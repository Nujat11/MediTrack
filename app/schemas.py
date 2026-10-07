import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr

# User Schemas
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    role: str
    created_at: datetime.datetime

    class Config:
        from_attributes = True

# Family Member Schemas
class FamilyMemberCreate(BaseModel):
    name: str
    relationship: str = "Self"
    age: Optional[int] = None
    gender: Optional[str] = None
    blood_group: Optional[str] = None
    chronic_conditions: Optional[str] = None
    allergies: Optional[str] = None
    emergency_contact: Optional[str] = None

class FamilyMemberResponse(BaseModel):
    id: int
    user_id: int
    name: str
    relationship: str
    age: Optional[int]
    gender: Optional[str]
    blood_group: Optional[str]
    chronic_conditions: Optional[str]
    allergies: Optional[str]
    emergency_contact: Optional[str]

    class Config:
        from_attributes = True

# Medication Schemas
class MedicationCreate(BaseModel):
    member_id: int
    brand_name: str
    generic_name: Optional[str] = None
    dosage_form: str = "Tablet"
    strength: Optional[str] = None
    schedule_pattern: str = "1+0+1"  # 1+0+1, 1+1+1, 1+0+0, 0+1+0, 0+0+1, SOS
    meal_timing: str = "খাওয়ার পরে (After Meal)"
    morning_time: str = "08:00"
    afternoon_time: str = "14:00"
    night_time: str = "21:30"
    bedtime_time: str = "23:00"
    start_date: datetime.date = datetime.date.today()
    end_date: Optional[datetime.date] = None
    is_chronic: bool = False
    doctor_name: Optional[str] = None
    instructions: Optional[str] = None

class MedicationResponse(BaseModel):
    id: int
    user_id: int
    member_id: int
    brand_name: str
    generic_name: Optional[str]
    dosage_form: str
    strength: Optional[str]
    schedule_pattern: str
    meal_timing: str
    morning_time: str
    afternoon_time: str
    night_time: str
    bedtime_time: str
    start_date: datetime.date
    end_date: Optional[datetime.date]
    is_chronic: bool
    is_active: bool
    doctor_name: Optional[str]
    instructions: Optional[str]

    class Config:
        from_attributes = True

# Dose Log Schemas
class DoseLogUpdate(BaseModel):
    medication_id: int
    member_id: int
    dose_date: datetime.date
    slot: str  # morning, afternoon, night, bedtime
    status: str  # taken, missed, skipped, pending
    notes: Optional[str] = None

# Appointment Schemas
class AppointmentCreate(BaseModel):
    member_id: int
    doctor_id: Optional[int] = None
    doctor_name: str
    specialty: Optional[str] = None
    chamber_name: str
    chamber_address: Optional[str] = None
    appointment_date: datetime.date
    appointment_time: str = "06:30 PM"
    serial_number: Optional[str] = None
    serial_contact: Optional[str] = None
    doctor_advice: Optional[str] = None
    follow_up_date: Optional[datetime.date] = None

class AppointmentResponse(BaseModel):
    id: int
    user_id: int
    member_id: int
    doctor_name: str
    specialty: Optional[str]
    chamber_name: str
    chamber_address: Optional[str]
    appointment_date: datetime.date
    appointment_time: str
    serial_number: Optional[str]
    serial_contact: Optional[str]
    status: str
    doctor_advice: Optional[str]
    follow_up_date: Optional[datetime.date]

    class Config:
        from_attributes = True

# Doctor Directory Schemas
class DoctorResponse(BaseModel):
    id: int
    name: str
    specialty: str
    degrees: str
    bmdc_reg_no: Optional[str]
    designation: Optional[str]
    hospital_affiliation: Optional[str]
    division: str
    district: str
    area: str
    chamber_name: str
    chamber_address: Optional[str]
    visiting_days: str
    visiting_hours: str
    serial_phone: str
    consultation_fee: int
    follow_up_fee: int

    class Config:
        from_attributes = True
