import datetime
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Medication, DoseLog, FamilyMember
from app.schemas import DoseLogUpdate
from app.auth import get_current_user

router = APIRouter(prefix="/api/tracking", tags=["Tracking & Adherence"])

def get_slots_for_pattern(pattern: str) -> List[str]:
    """Map Bangladeshi prescription notation to schedule slots"""
    p = pattern.strip().upper()
    if p == "1+0+1":
        return ["morning", "night"]
    elif p == "1+1+1":
        return ["morning", "afternoon", "night"]
    elif p == "1+0+0":
        return ["morning"]
    elif p == "0+1+0":
        return ["afternoon"]
    elif p == "0+0+1":
        return ["night"]
    elif p == "1+0+0+1":
        return ["morning", "bedtime"]
    elif "SOS" in p:
        return ["as_needed"]
    return ["morning", "night"]

@router.get("/timeline")
def get_daily_timeline(
    member_id: Optional[int] = None,
    target_date: Optional[datetime.date] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not target_date:
        target_date = datetime.date.today()

    # If no member_id specified, pick the first family member (e.g. Self)
    if not member_id:
        first_member = db.query(FamilyMember).filter(FamilyMember.user_id == current_user.id).first()
        if not first_member:
            return {"date": str(target_date), "slots": {}}
        member_id = first_member.id

    # Active medications for this member valid on target_date
    meds = db.query(Medication).filter(
        Medication.user_id == current_user.id,
        Medication.member_id == member_id,
        Medication.is_active == True,
        Medication.start_date <= target_date
    ).all()

    # Filter out finished non-chronic medications
    active_meds = [m for m in meds if m.is_chronic or (m.end_date and m.end_date >= target_date) or not m.end_date]

    # Existing logs for this date
    logs = db.query(DoseLog).filter(
        DoseLog.user_id == current_user.id,
        DoseLog.member_id == member_id,
        DoseLog.dose_date == target_date
    ).all()
    log_map = {(l.medication_id, l.slot): l for l in logs}

    timeline = {
        "morning": [],
        "afternoon": [],
        "night": [],
        "bedtime": [],
        "as_needed": []
    }

    slot_display_times = {
        "morning": "সকাল ০৮:০০ (Morning)",
        "afternoon": "দুপুর ০২:০০ (Afternoon)",
        "night": "রাত ০৯:৩০ (Night/Dinner)",
        "bedtime": "রাত ১১:০০ (Bedtime)",
        "as_needed": "প্রয়োজনে (SOS)"
    }

    for med in active_meds:
        slots = get_slots_for_pattern(med.schedule_pattern)
        for slot in slots:
            if slot not in timeline:
                timeline[slot] = []
            
            existing_log = log_map.get((med.id, slot))
            status = existing_log.status if existing_log else "pending"
            taken_at = existing_log.taken_at.strftime("%I:%M %p") if (existing_log and existing_log.taken_at) else None

            # Determine scheduled time display
            sched_time = getattr(med, f"{slot}_time", "08:00") if hasattr(med, f"{slot}_time") else "08:00"

            timeline[slot].append({
                "medication_id": med.id,
                "brand_name": med.brand_name,
                "generic_name": med.generic_name,
                "dosage_form": med.dosage_form,
                "strength": med.strength,
                "meal_timing": med.meal_timing,
                "scheduled_time": sched_time,
                "instructions": med.instructions,
                "status": status,
                "taken_at": taken_at,
                "log_id": existing_log.id if existing_log else None
            })

    total_doses = sum(len(doses) for s, doses in timeline.items() if s != "as_needed")
    taken_doses = sum(len([d for d in doses if d["status"] == "taken"]) for s, doses in timeline.items() if s != "as_needed")
    missed_doses = sum(len([d for d in doses if d["status"] == "missed"]) for s, doses in timeline.items() if s != "as_needed")
    pending_doses = total_doses - (taken_doses + missed_doses)

    return {
        "date": str(target_date),
        "member_id": member_id,
        "timeline": timeline,
        "summary": {
            "total": total_doses,
            "taken": taken_doses,
            "missed": missed_doses,
            "pending": pending_doses,
            "adherence_rate": round((taken_doses / total_doses * 100), 1) if total_doses > 0 else 100.0
        }
    }

@router.post("/log")
def log_dose(
    log_data: DoseLogUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify medication belongs to user
    med = db.query(Medication).filter(
        Medication.id == log_data.medication_id,
        Medication.user_id == current_user.id
    ).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found.")

    # Find or create DoseLog
    log = db.query(DoseLog).filter(
        DoseLog.medication_id == log_data.medication_id,
        DoseLog.dose_date == log_data.dose_date,
        DoseLog.slot == log_data.slot
    ).first()

    now = datetime.datetime.utcnow() + datetime.timedelta(hours=6) # Bangladesh Time GMT+6

    if not log:
        log = DoseLog(
            medication_id=log_data.medication_id,
            user_id=current_user.id,
            member_id=log_data.member_id,
            dose_date=log_data.dose_date,
            slot=log_data.slot,
            status=log_data.status,
            taken_at=now if log_data.status == "taken" else None,
            notes=log_data.notes
        )
        db.add(log)
    else:
        log.status = log_data.status
        log.taken_at = now if log_data.status == "taken" else None
        if log_data.notes:
            log.notes = log_data.notes

    db.commit()
    db.refresh(log)
    return {"status": "success", "log_id": log.id, "dose_status": log.status}

@router.get("/adherence")
def get_adherence_analytics(
    member_id: Optional[int] = None,
    days: int = Query(7, ge=3, le=90),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    today = datetime.date.today()
    start_date = today - datetime.timedelta(days=days - 1)

    query = db.query(DoseLog).filter(
        DoseLog.user_id == current_user.id,
        DoseLog.dose_date >= start_date,
        DoseLog.dose_date <= today
    )
    if member_id:
        query = query.filter(DoseLog.member_id == member_id)

    logs = query.all()

    taken_count = sum(1 for l in logs if l.status == "taken")
    missed_count = sum(1 for l in logs if l.status == "missed")
    total_logged = taken_count + missed_count
    
    adherence_percentage = round((taken_count / total_logged * 100), 1) if total_logged > 0 else 100.0

    # Daily breakdown for charts
    daily_stats = []
    for d in range(days):
        cur_date = start_date + datetime.timedelta(days=d)
        cur_logs = [l for l in logs if l.dose_date == cur_date]
        d_taken = sum(1 for l in cur_logs if l.status == "taken")
        d_missed = sum(1 for l in cur_logs if l.status == "missed")
        daily_stats.append({
            "date": cur_date.strftime("%d %b"),
            "taken": d_taken,
            "missed": d_missed
        })

    return {
        "period_days": days,
        "adherence_percentage": adherence_percentage,
        "total_taken": taken_count,
        "total_missed": missed_count,
        "daily_breakdown": daily_stats
    }
