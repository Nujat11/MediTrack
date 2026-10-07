from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.database import get_db
from app.models import Doctor
from app.schemas import DoctorResponse

router = APIRouter(prefix="/api/doctors", tags=["Doctor Directory"])

@router.get("", response_model=List[DoctorResponse])
def get_doctors(
    specialty: Optional[str] = None,
    division: Optional[str] = None,
    area: Optional[str] = None,
    q: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Doctor)

    if specialty and specialty.strip() != "All":
        query = query.filter(Doctor.specialty.ilike(f"%{specialty}%"))
    if division and division.strip() != "All":
        query = query.filter(Doctor.division == division)
    if area and area.strip() != "All":
        query = query.filter(Doctor.area.ilike(f"%{area}%"))
    if q and q.strip():
        term = q.strip()
        query = query.filter(
            or_(
                Doctor.name.ilike(f"%{term}%"),
                Doctor.chamber_name.ilike(f"%{term}%"),
                Doctor.specialty.ilike(f"%{term}%"),
                Doctor.hospital_affiliation.ilike(f"%{term}%")
            )
        )

    return query.all()

@router.get("/filters")
def get_doctor_filters(db: Session = Depends(get_db)):
    """Return distinct filter options for the search UI"""
    specialties = [s[0] for s in db.query(Doctor.specialty).distinct().all()]
    divisions = [d[0] for d in db.query(Doctor.division).distinct().all()]
    areas = [a[0] for a in db.query(Doctor.area).distinct().all()]

    return {
        "specialties": specialties,
        "divisions": divisions,
        "areas": areas
    }
