import os
from pathlib import Path
from fastapi import FastAPI, Request, Depends, HTTPException, Query, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import BASE_DIR, UPLOAD_DIR
from app.database import engine, Base, get_db, SessionLocal
from app.models import User, FamilyMember, Medication, Appointment, PrescriptionDocument, Doctor, MedicineCatalog, DoseLog
from app.seed_data import seed_database
from app.auth import get_optional_user

# Import Routers
from app.routers import (
    auth, medications, tracking, family, appointments, doctors, prescriptions, admin
)

# Initialize Database Schema
Base.metadata.create_all(bind=engine)

# Seed initial data
with SessionLocal() as db_session:
    seed_database(db_session)

app = FastAPI(
    title="MediTrack Bangladesh",
    description="A Web-Based Medication and Treatment Tracking System for Bangladeshi Patients and Caregivers",
    version="1.0.0"
)

# Mount Static Files and Uploads
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "app" / "static")), name="static")
app.mount("/uploads", StaticFiles(directory=str(UPLOAD_DIR)), name="uploads")

# Templates
ui_dir = BASE_DIR / "app" / "UI"
templates_dir = ui_dir if ui_dir.exists() else (BASE_DIR / "app" / "templates")
templates = Jinja2Templates(directory=str(templates_dir))

# Include API Routers
app.include_router(auth.router)
app.include_router(family.router)
app.include_router(medications.router)
app.include_router(tracking.router)
app.include_router(appointments.router)
app.include_router(doctors.router)
app.include_router(prescriptions.router)
app.include_router(admin.router)

# Helper function to get active member for user
def get_user_and_active_member(request: Request, db: Session, member_id: int = None):
    user = get_optional_user(request, db)
    if not user:
        return None, [], None

    members = db.query(FamilyMember).filter(FamilyMember.user_id == user.id).all()
    if not members:
        default_self = FamilyMember(
            user_id=user.id,
            name=f"{user.name} (Self)",
            relationship="Self",
            emergency_contact=user.phone
        )
        db.add(default_self)
        db.commit()
        db.refresh(default_self)
        members = [default_self]

    active = None
    if member_id:
        active = next((m for m in members if m.id == member_id), None)
    if not active and members:
        active = members[0]

    return user, members, active


# ------------------ FRONTEND WEB PAGE ROUTES ------------------

@app.get("/", response_class=HTMLResponse)
def index_page(request: Request, db: Session = Depends(get_db)):
    user = get_optional_user(request, db)
    if user:
        return RedirectResponse(url="/dashboard", status_code=302)
    return templates.TemplateResponse(request=request, name="index.html", context={
        "user": None,
        "active_page": "home"
    })

@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request, db: Session = Depends(get_db)):
    user = get_optional_user(request, db)
    if user:
        return RedirectResponse(url="/dashboard", status_code=302)
    return templates.TemplateResponse(request=request, name="login.html", context={
        "user": None,
        "active_page": "login"
    })

@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request, db: Session = Depends(get_db)):
    user = get_optional_user(request, db)
    if user:
        return RedirectResponse(url="/dashboard", status_code=302)
    return templates.TemplateResponse(request=request, name="register.html", context={
        "user": None,
        "active_page": "register"
    })

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(
    request: Request,
    member_id: int = Query(None),
    db: Session = Depends(get_db)
):
    user, members, active_member = get_user_and_active_member(request, db, member_id)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    # Fetch next upcoming appointment
    upcoming_apt = None
    if active_member:
        upcoming_apt = db.query(Appointment).filter(
            Appointment.user_id == user.id,
            Appointment.member_id == active_member.id,
            Appointment.status == "Upcoming"
        ).order_by(Appointment.appointment_date.asc()).first()

    return templates.TemplateResponse(request=request, name="dashboard.html", context={
        "user": user,
        "active_page": "dashboard",
        "family_members": members,
        "active_member": active_member,
        "upcoming_appointment": upcoming_apt
    })

@app.get("/medications", response_class=HTMLResponse)
def medications_page(
    request: Request,
    member_id: int = Query(None),
    db: Session = Depends(get_db)
):
    user, members, active_member = get_user_and_active_member(request, db, member_id)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    meds = []
    if active_member:
        meds = db.query(Medication).filter(
            Medication.user_id == user.id,
            Medication.member_id == active_member.id
        ).order_by(Medication.created_at.desc()).all()

    return templates.TemplateResponse(request=request, name="medications.html", context={
        "user": user,
        "active_page": "medications",
        "family_members": members,
        "active_member": active_member,
        "medications": meds
    })

@app.get("/doctors", response_class=HTMLResponse)
def doctors_page(
    request: Request,
    member_id: int = Query(None),
    db: Session = Depends(get_db)
):
    user, members, active_member = get_user_and_active_member(request, db, member_id)
    return templates.TemplateResponse(request=request, name="doctors.html", context={
        "user": user,
        "active_page": "doctors",
        "family_members": members,
        "active_member": active_member
    })

@app.get("/appointments", response_class=HTMLResponse)
def appointments_page(
    request: Request,
    member_id: int = Query(None),
    db: Session = Depends(get_db)
):
    user, members, active_member = get_user_and_active_member(request, db, member_id)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    apts = []
    if active_member:
        apts = db.query(Appointment).filter(
            Appointment.user_id == user.id,
            Appointment.member_id == active_member.id
        ).order_by(Appointment.appointment_date.asc()).all()

    return templates.TemplateResponse(request=request, name="appointments.html", context={
        "user": user,
        "active_page": "appointments",
        "family_members": members,
        "active_member": active_member,
        "appointments": apts
    })

@app.get("/prescriptions", response_class=HTMLResponse)
def prescriptions_page(
    request: Request,
    member_id: int = Query(None),
    db: Session = Depends(get_db)
):
    user, members, active_member = get_user_and_active_member(request, db, member_id)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    prescriptions_list = []
    if active_member:
        prescriptions_list = db.query(PrescriptionDocument).filter(
            PrescriptionDocument.user_id == user.id,
            PrescriptionDocument.member_id == active_member.id
        ).order_by(PrescriptionDocument.document_date.desc()).all()

    return templates.TemplateResponse(request=request, name="prescriptions.html", context={
        "user": user,
        "active_page": "prescriptions",
        "family_members": members,
        "active_member": active_member,
        "prescriptions": prescriptions_list
    })

@app.get("/family", response_class=HTMLResponse)
def family_page(
    request: Request,
    member_id: int = Query(None),
    db: Session = Depends(get_db)
):
    user, members, active_member = get_user_and_active_member(request, db, member_id)
    if not user:
        return RedirectResponse(url="/login", status_code=302)

    return templates.TemplateResponse(request=request, name="family.html", context={
        "user": user,
        "active_page": "family",
        "family_members": members,
        "active_member": active_member
    })

@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request, db: Session = Depends(get_db)):
    user = get_optional_user(request, db)
    if not user or user.role != "admin":
        return RedirectResponse(url="/dashboard", status_code=302)

    stats = {
        "total_users": db.query(User).count(),
        "active_medications": db.query(Medication).filter(Medication.is_active == True).count(),
        "total_doses_logged": db.query(DoseLog).count(),
        "total_catalog_medicines": db.query(MedicineCatalog).count(),
        "total_doctors": db.query(Doctor).count()
    }
    all_users = db.query(User).all()

    return templates.TemplateResponse(request=request, name="admin.html", context={
        "user": user,
        "active_page": "admin",
        "stats": stats,
        "users": all_users
    })
