from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database import get_db
from app.models import User, Medication, MedicineCatalog, FamilyMember
from app.schemas import MedicationCreate, MedicationResponse
from app.auth import get_current_user

router = APIRouter(prefix="/api/medications", tags=["Medications"])

@router.get("/catalog/search")
def search_catalog(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    """Search pre-seeded Bangladeshi pharmaceuticals by brand or generic name"""
    results = db.query(MedicineCatalog).filter(
        or_(
            MedicineCatalog.brand_name.ilike(f"%{q}%"),
            MedicineCatalog.generic_name.ilike(f"%{q}%"),
            MedicineCatalog.manufacturer.ilike(f"%{q}%")
        )
    ).limit(10).all()
    
    return [
        {
            "id": m.id,
            "brand_name": m.brand_name,
            "generic_name": m.generic_name,
            "dosage_form": m.dosage_form,
            "strength": m.strength,
            "manufacturer": m.manufacturer,
            "therapeutic_category": m.therapeutic_category
        }
        for m in results
    ]

@router.get("", response_model=List[MedicationResponse])
def get_medications(
    member_id: Optional[int] = None,
    is_active: Optional[bool] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Medication).filter(Medication.user_id == current_user.id)
    if member_id:
        query = query.filter(Medication.member_id == member_id)
    if is_active is not None:
        query = query.filter(Medication.is_active == is_active)
    return query.order_by(Medication.created_at.desc()).all()

@router.post("", response_model=MedicationResponse)
def add_medication(
    med_data: MedicationCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify the member belongs to the current user
    member = db.query(FamilyMember).filter(
        FamilyMember.id == med_data.member_id,
        FamilyMember.user_id == current_user.id
    ).first()
    if not member:
        raise HTTPException(status_code=400, detail="Invalid family member profile.")

    new_med = Medication(
        user_id=current_user.id,
        member_id=med_data.member_id,
        brand_name=med_data.brand_name,
        generic_name=med_data.generic_name,
        dosage_form=med_data.dosage_form,
        strength=med_data.strength,
        schedule_pattern=med_data.schedule_pattern,
        meal_timing=med_data.meal_timing,
        morning_time=med_data.morning_time,
        afternoon_time=med_data.afternoon_time,
        night_time=med_data.night_time,
        bedtime_time=med_data.bedtime_time,
        start_date=med_data.start_date,
        end_date=med_data.end_date,
        is_chronic=med_data.is_chronic,
        doctor_name=med_data.doctor_name,
        instructions=med_data.instructions
    )
    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return new_med

@router.put("/{med_id}/toggle-status")
def toggle_medication_status(
    med_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    med = db.query(Medication).filter(
        Medication.id == med_id,
        Medication.user_id == current_user.id
    ).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found.")

    med.is_active = not med.is_active
    db.commit()
    return {"status": "success", "is_active": med.is_active}

@router.delete("/{med_id}")
def delete_medication(
    med_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    med = db.query(Medication).filter(
        Medication.id == med_id,
        Medication.user_id == current_user.id
    ).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found.")

    db.delete(med)
    db.commit()
    return {"status": "success", "message": "Medication removed successfully."}
