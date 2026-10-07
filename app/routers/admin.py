from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, MedicineCatalog, Doctor, Medication, DoseLog
from app.auth import get_current_admin

router = APIRouter(prefix="/api/admin", tags=["Admin Portal"])

class MedicineCreateRequest(BaseModel):
    brand_name: str
    generic_name: str
    dosage_form: str = "Tablet"
    strength: Optional[str] = None
    manufacturer: Optional[str] = None
    therapeutic_category: Optional[str] = None

class DoctorCreateRequest(BaseModel):
    name: str
    specialty: str
    degrees: str
    bmdc_reg_no: Optional[str] = None
    designation: Optional[str] = None
    hospital_affiliation: Optional[str] = None
    division: str = "Dhaka"
    district: str = "Dhaka"
    area: str
    chamber_name: str
    chamber_address: Optional[str] = None
    visiting_days: str = "Saturday - Thursday"
    visiting_hours: str = "5:00 PM - 9:00 PM"
    serial_phone: str
    consultation_fee: int = 1000
    follow_up_fee: int = 600

@router.get("/stats")
def get_system_statistics(admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    total_users = db.query(User).count()
    total_medications = db.query(Medication).count()
    active_medications = db.query(Medication).filter(Medication.is_active == True).count()
    total_doses_logged = db.query(DoseLog).count()
    total_catalog_medicines = db.query(MedicineCatalog).count()
    total_doctors = db.query(Doctor).count()

    return {
        "total_users": total_users,
        "total_medications": total_medications,
        "active_medications": active_medications,
        "total_doses_logged": total_doses_logged,
        "total_catalog_medicines": total_catalog_medicines,
        "total_doctors": total_doctors
    }

@router.post("/medicines")
def add_catalog_medicine(
    med: MedicineCreateRequest,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    new_med = MedicineCatalog(
        brand_name=med.brand_name,
        generic_name=med.generic_name,
        dosage_form=med.dosage_form,
        strength=med.strength,
        manufacturer=med.manufacturer,
        therapeutic_category=med.therapeutic_category
    )
    db.add(new_med)
    db.commit()
    db.refresh(new_med)
    return {"status": "success", "medicine": new_med.brand_name}

@router.delete("/medicines/{med_id}")
def delete_catalog_medicine(
    med_id: int,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    med = db.query(MedicineCatalog).filter(MedicineCatalog.id == med_id).first()
    if not med:
        raise HTTPException(status_code=404, detail="Medicine not found.")
    db.delete(med)
    db.commit()
    return {"status": "success", "message": "Medicine removed."}

@router.post("/doctors")
def add_doctor(
    doc: DoctorCreateRequest,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    new_doc = Doctor(
        name=doc.name,
        specialty=doc.specialty,
        degrees=doc.degrees,
        bmdc_reg_no=doc.bmdc_reg_no,
        designation=doc.designation,
        hospital_affiliation=doc.hospital_affiliation,
        division=doc.division,
        district=doc.district,
        area=doc.area,
        chamber_name=doc.chamber_name,
        chamber_address=doc.chamber_address,
        visiting_days=doc.visiting_days,
        visiting_hours=doc.visiting_hours,
        serial_phone=doc.serial_phone,
        consultation_fee=doc.consultation_fee,
        follow_up_fee=doc.follow_up_fee
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return {"status": "success", "doctor": new_doc.name}

@router.delete("/doctors/{doc_id}")
def delete_doctor(
    doc_id: int,
    admin: User = Depends(get_current_admin),
    db: Session = Depends(get_db)
):
    doc = db.query(Doctor).filter(Doctor.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Doctor not found.")
    db.delete(doc)
    db.commit()
    return {"status": "success", "message": "Doctor removed."}

@router.get("/users")
def get_user_list(admin: User = Depends(get_current_admin), db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "phone": u.phone,
            "role": u.role,
            "created_at": str(u.created_at)
        }
        for u in users
    ]
