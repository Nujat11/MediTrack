import datetime
from sqlalchemy import (
    Column, Integer, String, Text, Boolean, Date, DateTime, ForeignKey, Float
)
from sqlalchemy.orm import relationship as orm_relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    phone = Column(String(20), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(20), default="user")  # "user" or "admin"
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    family_members = orm_relationship("FamilyMember", back_populates="user", cascade="all, delete-orphan")
    medications = orm_relationship("Medication", back_populates="user", cascade="all, delete-orphan")
    dose_logs = orm_relationship("DoseLog", back_populates="user", cascade="all, delete-orphan")
    appointments = orm_relationship("Appointment", back_populates="user", cascade="all, delete-orphan")
    prescriptions = orm_relationship("PrescriptionDocument", back_populates="user", cascade="all, delete-orphan")


class FamilyMember(Base):
    """Profiles for dependents / elderly parents in the Bangladeshi family context"""
    __tablename__ = "family_members"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False)
    
    # Store relationship type as string, column name in db is 'relationship'
    relationship_type = Column("relationship", String(50), default="Self")
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)  # Male, Female, Other
    blood_group = Column(String(10), nullable=True)  # A+, A-, B+, B-, O+, O-, AB+, AB-
    chronic_conditions = Column(String(255), nullable=True)  # e.g. Diabetes, Hypertension, CKD, Asthma
    allergies = Column(String(255), nullable=True)
    emergency_contact = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def relationship(self):
        return self.relationship_type

    @relationship.setter
    def relationship(self, value):
        self.relationship_type = value

    # ORM Relationships
    user = orm_relationship("User", back_populates="family_members")
    medications = orm_relationship("Medication", back_populates="family_member", cascade="all, delete-orphan")
    dose_logs = orm_relationship("DoseLog", back_populates="family_member", cascade="all, delete-orphan")
    appointments = orm_relationship("Appointment", back_populates="family_member", cascade="all, delete-orphan")
    prescriptions = orm_relationship("PrescriptionDocument", back_populates="family_member", cascade="all, delete-orphan")


class MedicineCatalog(Base):
    """Master database of Bangladeshi pharmaceutical brand and generic medicines"""
    __tablename__ = "medicine_catalog"

    id = Column(Integer, primary_key=True, index=True)
    brand_name = Column(String(120), index=True, nullable=False)
    generic_name = Column(String(120), index=True, nullable=False)
    dosage_form = Column(String(50), default="Tablet")  # Tablet, Capsule, Syrup, Inhaler, Drop, Injection
    strength = Column(String(50), nullable=True)  # e.g., 500mg, 20mg, 10mg
    manufacturer = Column(String(100), nullable=True)  # Square, Beximco, Incepta, Renata, etc.
    therapeutic_category = Column(String(100), nullable=True)  # Gastric, Pain, Diabetes, Hypertension, Antibiotic


class Medication(Base):
    """User-scheduled medicines incorporating Bangladeshi prescription norms"""
    __tablename__ = "medications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("family_members.id"), nullable=False)
    
    brand_name = Column(String(120), nullable=False)
    generic_name = Column(String(120), nullable=True)
    dosage_form = Column(String(50), default="Tablet")
    strength = Column(String(50), nullable=True)

    # Bangladeshi prescription notation: 1+0+1, 1+1+1, 1+0+0, 0+1+0, 0+0+1, 1+0+0+1, SOS
    schedule_pattern = Column(String(20), default="1+0+1")
    # Relation to meal: খাওয়ার পরে, খাওয়ার আগে, খালি পেটে, শোবার আগে
    meal_timing = Column(String(50), default="খাওয়ার পরে (After Meal)")
    
    # Specific standard hours in 24-hr format
    morning_time = Column(String(10), default="08:00")
    afternoon_time = Column(String(10), default="14:00")
    night_time = Column(String(10), default="21:30")
    bedtime_time = Column(String(10), default="23:00")

    start_date = Column(Date, default=datetime.date.today)
    end_date = Column(Date, nullable=True)
    is_chronic = Column(Boolean, default=False)  # True for lifelong maintenance (BP/Sugar)
    is_active = Column(Boolean, default=True)

    doctor_name = Column(String(100), nullable=True)
    instructions = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user = orm_relationship("User", back_populates="medications")
    family_member = orm_relationship("FamilyMember", back_populates="medications")
    dose_logs = orm_relationship("DoseLog", back_populates="medication", cascade="all, delete-orphan")


class DoseLog(Base):
    """Tracking taken and missed doses with adherence metrics"""
    __tablename__ = "dose_logs"

    id = Column(Integer, primary_key=True, index=True)
    medication_id = Column(Integer, ForeignKey("medications.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("family_members.id"), nullable=False)

    dose_date = Column(Date, default=datetime.date.today, index=True)
    slot = Column(String(20), nullable=False)  # morning, afternoon, night, bedtime
    status = Column(String(20), default="pending")  # taken, missed, skipped, pending
    taken_at = Column(DateTime, nullable=True)
    notes = Column(String(255), nullable=True)

    # Relationships
    medication = orm_relationship("Medication", back_populates="dose_logs")
    user = orm_relationship("User", back_populates="dose_logs")
    family_member = orm_relationship("FamilyMember", back_populates="dose_logs")


class Doctor(Base):
    """Bangladeshi specialist doctor and private evening chamber directory"""
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    specialty = Column(String(100), index=True, nullable=False)
    degrees = Column(String(200), nullable=False)  # e.g. MBBS, FCPS, MD, MRCP
    bmdc_reg_no = Column(String(50), nullable=True)  # BMDC Registration number
    designation = Column(String(120), nullable=True)  # Professor / Associate Professor
    hospital_affiliation = Column(String(150), nullable=True)  # DMCH, BSMMU, NICVD, BIRDEM
    
    division = Column(String(50), index=True, default="Dhaka")
    district = Column(String(50), index=True, default="Dhaka")
    area = Column(String(100), index=True, nullable=False)  # Dhanmondi, Mirpur, Uttara, etc.
    
    chamber_name = Column(String(150), nullable=False)  # Popular, Ibn Sina, Labaid, etc.
    chamber_address = Column(String(255), nullable=True)
    visiting_days = Column(String(120), default="Saturday - Thursday")
    visiting_hours = Column(String(100), default="5:00 PM - 9:30 PM")
    serial_phone = Column(String(120), nullable=False)  # Chamber calling serial phone
    consultation_fee = Column(Integer, default=1000)
    follow_up_fee = Column(Integer, default=600)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    appointments = orm_relationship("Appointment", back_populates="doctor")


class Appointment(Base):
    """Chamber appointments and follow-up serial tracking in Bangladesh"""
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("family_members.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=True)

    doctor_name = Column(String(120), nullable=False)
    specialty = Column(String(100), nullable=True)
    chamber_name = Column(String(150), nullable=False)
    chamber_address = Column(String(255), nullable=True)

    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(String(50), default="06:30 PM")
    serial_number = Column(String(50), nullable=True)  # সিরিয়াল নম্বর (e.g. Serial #12)
    serial_contact = Column(String(100), nullable=True)

    status = Column(String(20), default="Upcoming")  # Upcoming, Completed, Cancelled
    doctor_advice = Column(Text, nullable=True)
    follow_up_date = Column(Date, nullable=True)  # পরবর্তী সাক্ষাতের তারিখ
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationships
    user = orm_relationship("User", back_populates="appointments")
    family_member = orm_relationship("FamilyMember", back_populates="appointments")
    doctor = orm_relationship("Doctor", back_populates="appointments")


class PrescriptionDocument(Base):
    """Digital prescription file vault to safeguard physical paper slips"""
    __tablename__ = "prescription_documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    member_id = Column(Integer, ForeignKey("family_members.id"), nullable=False)

    title = Column(String(150), nullable=False)
    doctor_name = Column(String(120), nullable=True)
    hospital_clinic = Column(String(150), nullable=True)
    document_date = Column(Date, default=datetime.date.today)
    
    file_path = Column(String(255), nullable=False)
    file_type = Column(String(50), default="image")  # image or pdf
    diagnosis_summary = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user = orm_relationship("User", back_populates="prescriptions")
    family_member = orm_relationship("FamilyMember", back_populates="prescriptions")
