import os
import shutil
import datetime
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, PrescriptionDocument, FamilyMember
from app.config import UPLOAD_DIR
from app.auth import get_current_user

router = APIRouter(prefix="/api/prescriptions", tags=["Prescription Vault"])

@router.get("")
def get_prescriptions(
    member_id: Optional[int] = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(PrescriptionDocument).filter(PrescriptionDocument.user_id == current_user.id)
    if member_id:
        query = query.filter(PrescriptionDocument.member_id == member_id)
    
    docs = query.order_by(PrescriptionDocument.document_date.desc()).all()
    return [
        {
            "id": d.id,
            "title": d.title,
            "doctor_name": d.doctor_name,
            "hospital_clinic": d.hospital_clinic,
            "document_date": str(d.document_date),
            "file_path": d.file_path,
            "file_type": d.file_type,
            "diagnosis_summary": d.diagnosis_summary,
            "member_id": d.member_id
        }
        for d in docs
    ]

@router.post("")
def upload_prescription(
    member_id: int = Form(...),
    title: str = Form(...),
    doctor_name: Optional[str] = Form(None),
    hospital_clinic: Optional[str] = Form(None),
    document_date: Optional[str] = Form(None),
    diagnosis_summary: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    member = db.query(FamilyMember).filter(
        FamilyMember.id == member_id,
        FamilyMember.user_id == current_user.id
    ).first()
    if not member:
        raise HTTPException(status_code=400, detail="Invalid family member.")

    saved_file_path = "/static/images/prescription_placeholder.png"
    file_type = "image"

    if file and file.filename:
        # Generate safe file name
        ext = os.path.splitext(file.filename)[1].lower()
        if ext in [".pdf"]:
            file_type = "pdf"
        elif ext in [".png", ".jpg", ".jpeg", ".webp"]:
            file_type = "image"
        else:
            file_type = "document"

        timestamp = int(datetime.datetime.utcnow().timestamp())
        safe_filename = f"rx_{current_user.id}_{member_id}_{timestamp}{ext}"
        destination = UPLOAD_DIR / safe_filename

        with open(destination, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        saved_file_path = f"/uploads/{safe_filename}"

    doc_date = datetime.date.fromisoformat(document_date) if document_date else datetime.date.today()

    new_doc = PrescriptionDocument(
        user_id=current_user.id,
        member_id=member_id,
        title=title,
        doctor_name=doctor_name,
        hospital_clinic=hospital_clinic,
        document_date=doc_date,
        file_path=saved_file_path,
        file_type=file_type,
        diagnosis_summary=diagnosis_summary
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    return {"status": "success", "id": new_doc.id, "title": new_doc.title}

@router.delete("/{doc_id}")
def delete_prescription(
    doc_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    doc = db.query(PrescriptionDocument).filter(
        PrescriptionDocument.id == doc_id,
        PrescriptionDocument.user_id == current_user.id
    ).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found.")

    db.delete(doc)
    db.commit()
    return {"status": "success", "message": "Document deleted."}
