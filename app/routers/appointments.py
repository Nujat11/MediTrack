from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, Appointment, FamilyMember, Doctor
from app.schemas import AppointmentCreate, AppointmentResponse
from app.auth import get_current_user

router = APIRouter(prefix="/api/appointments", tags=["Appointments & Chambers"])

@router.get("", response_model=List[AppointmentResponse])
def get_appointments(
    member_id: Optional[int] = None,
    status: Optional[str] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Appointment).filter(Appointment.user_id == current_user.id)
    if member_id:
        query = query.filter(Appointment.member_id == member_id)
    if status and status != "All":
        query = query.filter(Appointment.status == status)
    
    return query.order_by(Appointment.appointment_date.asc()).all()

@router.post("", response_model=AppointmentResponse)
def create_appointment(
    apt_data: AppointmentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # Verify family member
    member = db.query(FamilyMember).filter(
        FamilyMember.id == apt_data.member_id,
        FamilyMember.user_id == current_user.id
    ).first()
    if not member:
        raise HTTPException(status_code=400, detail="Invalid family member profile.")

    new_apt = Appointment(
        user_id=current_user.id,
        member_id=apt_data.member_id,
        doctor_id=apt_data.doctor_id,
        doctor_name=apt_data.doctor_name,
        specialty=apt_data.specialty,
        chamber_name=apt_data.chamber_name,
        chamber_address=apt_data.chamber_address,
        appointment_date=apt_data.appointment_date,
        appointment_time=apt_data.appointment_time,
        serial_number=apt_data.serial_number,
        serial_contact=apt_data.serial_contact,
        doctor_advice=apt_data.doctor_advice,
        follow_up_date=apt_data.follow_up_date,
        status="Upcoming"
    )
    db.add(new_apt)
    db.commit()
    db.refresh(new_apt)
    return new_apt

@router.put("/{apt_id}/status")
def update_appointment_status(
    apt_id: int,
    status: str = Query(..., pattern="^(Upcoming|Completed|Cancelled)$"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    apt = db.query(Appointment).filter(
        Appointment.id == apt_id,
        Appointment.user_id == current_user.id
    ).first()
    if not apt:
        raise HTTPException(status_code=404, detail="Appointment not found.")

    apt.status = status
    db.commit()
    return {"status": "success", "new_status": apt.status}

@router.delete("/{apt_id}")
def delete_appointment(
    apt_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    apt = db.query(Appointment).filter(
        Appointment.id == apt_id,
        Appointment.user_id == current_user.id
    ).first()
    if not apt:
        raise HTTPException(status_code=404, detail="Appointment not found.")

    db.delete(apt)
    db.commit()
    return {"status": "success", "message": "Appointment deleted."}
