import datetime
from sqlalchemy.orm import Session
from app.models import (
    User, FamilyMember, MedicineCatalog, Medication, DoseLog, Doctor, Appointment, PrescriptionDocument
)
from app.auth import hash_password

def seed_database(db: Session):
    # Check if already seeded
    if db.query(MedicineCatalog).first() is not None:
        return

    print("Seeding Bangladeshi Medicine Catalog...")
    medicines = [
        MedicineCatalog(
            brand_name="Napa Extra",
            generic_name="Paracetamol 500mg + Caffeine 65mg",
            dosage_form="Tablet",
            strength="500mg + 65mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Pain & Fever (জ্বর ও ব্যথা)"
        ),
        MedicineCatalog(
            brand_name="Napa 500mg",
            generic_name="Paracetamol",
            dosage_form="Tablet",
            strength="500mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Pain & Fever (জ্বর ও সাধারণ ব্যথা)"
        ),
        MedicineCatalog(
            brand_name="Seclo 20",
            generic_name="Omeprazole",
            dosage_form="Capsule",
            strength="20mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Gastric & Acidity (গ্যাস্ট্রিক ও এসিডিটি)"
        ),
        MedicineCatalog(
            brand_name="Sergel 20",
            generic_name="Esomeprazole",
            dosage_form="Capsule",
            strength="20mg",
            manufacturer="Healthcare Pharmaceuticals Ltd.",
            therapeutic_category="Gastric & Acidity (গ্যাস্ট্রিক ও আলসার)"
        ),
        MedicineCatalog(
            brand_name="Maxpro 20",
            generic_name="Esomeprazole",
            dosage_form="Tablet",
            strength="20mg",
            manufacturer="Renata Limited",
            therapeutic_category="Gastric & Acidity (গ্যাস্ট্রিক ও বুকজ্বালা)"
        ),
        MedicineCatalog(
            brand_name="Pantonix 20",
            generic_name="Pantoprazole",
            dosage_form="Tablet",
            strength="20mg",
            manufacturer="Incepta Pharmaceuticals Ltd.",
            therapeutic_category="Gastric & Acidity (গ্যাস্ট্রিক সমস্যা)"
        ),
        MedicineCatalog(
            brand_name="Monas 10",
            generic_name="Montelukast Sodium",
            dosage_form="Tablet",
            strength="10mg",
            manufacturer="Incepta Pharmaceuticals Ltd.",
            therapeutic_category="Respiratory & Asthma (হাঁপানি ও অ্যালার্জিজনিত শ্বাসকষ্ট)"
        ),
        MedicineCatalog(
            brand_name="Bizoran 5/20",
            generic_name="Amlodipine 5mg + Olmesartan Medoxomil 20mg",
            dosage_form="Tablet",
            strength="5mg/20mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Hypertension (উচ্চ রক্তচাপ / প্রেসার)"
        ),
        MedicineCatalog(
            brand_name="Gluconor 500",
            generic_name="Metformin Hydrochloride",
            dosage_form="Tablet",
            strength="500mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Diabetes (ডায়াবেটিস নিয়ন্ত্রণ)"
        ),
        MedicineCatalog(
            brand_name="Ace Plus",
            generic_name="Paracetamol + Caffeine",
            dosage_form="Tablet",
            strength="500mg + 65mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Pain & Headache (মাথাব্যথা ও জ্বর)"
        ),
        MedicineCatalog(
            brand_name="Alatrol 10",
            generic_name="Cetirizine Hydrochloride",
            dosage_form="Tablet",
            strength="10mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Allergy & Cold (সর্দি, হাঁচি ও অ্যালার্জি)"
        ),
        MedicineCatalog(
            brand_name="Ciprocin 500",
            generic_name="Ciprofloxacin",
            dosage_form="Tablet",
            strength="500mg",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Antibiotic (অ্যান্টিবায়োটিক)"
        ),
        MedicineCatalog(
            brand_name="Azith 500",
            generic_name="Azithromycin",
            dosage_form="Tablet",
            strength="500mg",
            manufacturer="Beximco Pharmaceuticals Ltd.",
            therapeutic_category="Antibiotic (অ্যান্টিবায়োটিক সংক্রমণ)"
        ),
        MedicineCatalog(
            brand_name="Rosuva 10",
            generic_name="Rosuvastatin Calcium",
            dosage_form="Tablet",
            strength="10mg",
            manufacturer="Incepta Pharmaceuticals Ltd.",
            therapeutic_category="Cholesterol & Heart (কোলেস্টেরল ও হৃদরোগ)"
        ),
        MedicineCatalog(
            brand_name="Bicozin",
            generic_name="Vitamin B-Complex + Zinc",
            dosage_form="Syrup",
            strength="100ml",
            manufacturer="Square Pharmaceuticals PLC",
            therapeutic_category="Vitamin Supplement (ভিটামিন ও জিংক)"
        ),
        MedicineCatalog(
            brand_name="Thyrox 50",
            generic_name="Levothyroxine Sodium",
            dosage_form="Tablet",
            strength="50mcg",
            manufacturer="Popular Pharmaceuticals Ltd.",
            therapeutic_category="Thyroid Hormone (থাইরয়েড হরমোন)"
        )
    ]
    db.add_all(medicines)
    db.commit()

    print("Seeding Bangladeshi Specialist Doctors & Evening Chambers...")
    doctors = [
        Doctor(
            name="Prof. Dr. M. A. Hasan",
            specialty="Medicine & Diabetology (মেডিসিন ও ডায়াবেটিস)",
            degrees="MBBS, FCPS (Medicine), MD (Endocrinology), MACP (USA)",
            bmdc_reg_no="A-31284",
            designation="Professor & Head of Department",
            hospital_affiliation="Dhaka Medical College & Hospital (DMCH)",
            division="Dhaka",
            district="Dhaka",
            area="Dhanmondi",
            chamber_name="Popular Diagnostic Centre Ltd., Dhanmondi Branch",
            chamber_address="House #16, Road #2, Dhanmondi, Dhaka-1205 (Room 304)",
            visiting_days="Saturday - Thursday (শনিবার - বৃহস্পতিবার)",
            visiting_hours="5:30 PM - 9:30 PM",
            serial_phone="09613-787801, 01711-392810",
            consultation_fee=1200,
            follow_up_fee=700
        ),
        Doctor(
            name="Dr. Sabrina Rahman",
            specialty="Cardiology & Heart Disease (কার্ডিওলজি ও হৃদরোগ)",
            degrees="MBBS, MD (Cardiology), NICVD, FACC (USA)",
            bmdc_reg_no="A-45920",
            designation="Associate Professor",
            hospital_affiliation="National Institute of Cardiovascular Diseases (NICVD)",
            division="Dhaka",
            district="Dhaka",
            area="Panthapath",
            chamber_name="Square Hospital & Consultation Centre",
            chamber_address="18/F, Bir Uttam Qazi Nuruzzaman Sarak, Panthapath, Dhaka",
            visiting_days="Sunday - Wednesday (রবি - বুধ)",
            visiting_hours="6:00 PM - 10:00 PM",
            serial_phone="10616, 01713-377775",
            consultation_fee=1500,
            follow_up_fee=1000
        ),
        Doctor(
            name="Prof. Dr. Syed Anwarul Karim",
            specialty="Neurology & Stroke Specialist (নিউরোমেডিসিন)",
            degrees="MBBS, FCPS (Medicine), MD (Neurology)",
            bmdc_reg_no="A-28945",
            designation="Professor of Neuromedicine",
            hospital_affiliation="Bangabandhu Sheikh Mujib Medical University (BSMMU)",
            division="Dhaka",
            district="Dhaka",
            area="Shantinagar",
            chamber_name="Popular Diagnostic Centre, Shantinagar Branch",
            chamber_address="Unit 1, House 11, Shantinagar, Dhaka",
            visiting_days="Saturday - Wednesday (শনি - বুধ)",
            visiting_hours="5:00 PM - 8:30 PM",
            serial_phone="09613-787803, 01722-554433",
            consultation_fee=1400,
            follow_up_fee=800
        ),
        Doctor(
            name="Dr. Farhana Yasmin",
            specialty="Pediatrics & Child Health (শিশু রোগ বিশেষজ্ঞ)",
            degrees="MBBS, DCH, FCPS (Pediatrics)",
            bmdc_reg_no="A-51203",
            designation="Assistant Professor",
            hospital_affiliation="Dhaka Shishu (Children) Hospital",
            division="Dhaka",
            district="Dhaka",
            area="Mirpur",
            chamber_name="Ibn Sina Diagnostic & Consultation Center, Mirpur",
            chamber_address="House 11, Avenue 3, Section 11, Mirpur, Dhaka-1216",
            visiting_days="Saturday - Thursday (শনি - বৃহস্পতি)",
            visiting_hours="6:00 PM - 9:00 PM",
            serial_phone="09610-010615, 01819-234567",
            consultation_fee=1000,
            follow_up_fee=600
        ),
        Doctor(
            name="Prof. Dr. M. R. Chowdhury",
            specialty="Orthopedics & Spine Surgery (অর্থোপেডিক ও ট্রমা)",
            degrees="MBBS, MS (Orthopedics), Fellow WHO",
            bmdc_reg_no="A-22119",
            designation="Former Professor & Director",
            hospital_affiliation="National Institute of Traumatology & Rehabilitation (NITOR - পঙ্গু হাসপাতাল)",
            division="Dhaka",
            district="Dhaka",
            area="Uttara",
            chamber_name="Labaid Diagnostic, Uttara Branch",
            chamber_address="House 15, Road 13, Sector 3, Uttara, Dhaka-1230",
            visiting_days="Saturday - Wednesday (শনি - বুধ)",
            visiting_hours="5:30 PM - 9:00 PM",
            serial_phone="10606, 01766-662888",
            consultation_fee=1200,
            follow_up_fee=700
        ),
        Doctor(
            name="Dr. Tanvir Ahmed Chowdhury",
            specialty="Nephrology & Kidney Disease (কিডনি রোগ বিশেষজ্ঞ)",
            degrees="MBBS, MD (Nephrology), BSMMU",
            bmdc_reg_no="A-48301",
            designation="Associate Professor",
            hospital_affiliation="Chattogram Medical College Hospital (CMCH)",
            division="Chattogram",
            district="Chattogram",
            area="Panchlaish",
            chamber_name="Chevron Clinical Laboratory & Diagnostic Centre",
            chamber_address="12/12 O.R. Nizam Road, Panchlaish, Chattogram",
            visiting_days="Saturday - Thursday (শনি - বৃহস্পতি)",
            visiting_hours="5:00 PM - 9:00 PM",
            serial_phone="031-652533, 01711-789012",
            consultation_fee=1000,
            follow_up_fee=600
        )
    ]
    db.add_all(doctors)
    db.commit()

    print("Seeding Demo Users, Caregiver Family Members & Prescriptions...")
    # 1. Admin User
    admin = User(
        name="System Admin (MediTrack BD)",
        email="admin@meditrack.bd",
        phone="01710000000",
        hashed_password=hash_password("admin123"),
        role="admin"
    )
    db.add(admin)

    # 2. Regular User (Ariful Islam - Caregiver managing for himself and parents)
    user = User(
        name="Ariful Islam",
        email="demo@meditrack.bd",
        phone="01712345678",
        hashed_password=hash_password("password123"),
        role="user"
    )
    db.add(user)
    db.commit()

    # Family Members
    self_member = FamilyMember(
        user_id=user.id,
        name="Ariful Islam (Self)",
        relationship="Self",
        age=29,
        gender="Male",
        blood_group="B+",
        chronic_conditions="None (Seasonal Allergic Rhinitis)",
        allergies="Dust, Cold weather",
        emergency_contact="01712345678"
    )
    father_member = FamilyMember(
        user_id=user.id,
        name="Abdul Karim (বাবা)",
        relationship="Father",
        age=63,
        gender="Male",
        blood_group="O+",
        chronic_conditions="Type-2 Diabetes, Hypertension (উচ্চ রক্তচাপ)",
        allergies="None known",
        emergency_contact="01712345678"
    )
    mother_member = FamilyMember(
        user_id=user.id,
        name="Sufia Begum (মা)",
        relationship="Mother",
        age=57,
        gender="Female",
        blood_group="A+",
        chronic_conditions="Osteoarthritis (হাঁটু ব্যথা), Chronic Gastritis",
        allergies="Sulfa drugs",
        emergency_contact="01712345678"
    )
    db.add_all([self_member, father_member, mother_member])
    db.commit()

    today = datetime.date.today()

    # Father's Medications (Classic BD chronic regimen)
    med1 = Medication(
        user_id=user.id,
        member_id=father_member.id,
        brand_name="Bizoran 5/20",
        generic_name="Amlodipine + Olmesartan",
        dosage_form="Tablet",
        strength="5mg/20mg",
        schedule_pattern="1+0+0",
        meal_timing="খাওয়ার পরে (After Breakfast)",
        morning_time="08:30",
        start_date=today - datetime.timedelta(days=60),
        is_chronic=True,
        is_active=True,
        doctor_name="Prof. Dr. M. A. Hasan (DMCH)",
        instructions="সকালে নাস্তার পর ১টি। প্রেসার নিয়ন্ত্রণে না থাকলে বাদ দেবেন না।"
    )
    med2 = Medication(
        user_id=user.id,
        member_id=father_member.id,
        brand_name="Gluconor 500",
        generic_name="Metformin Hydrochloride",
        dosage_form="Tablet",
        strength="500mg",
        schedule_pattern="1+0+1",
        meal_timing="খাওয়ার পরে (After Meals)",
        morning_time="08:30",
        night_time="21:30",
        start_date=today - datetime.timedelta(days=90),
        is_chronic=True,
        is_active=True,
        doctor_name="Prof. Dr. M. A. Hasan (DMCH)",
        instructions="সকালে ও রাতে ভারী খাবার/ভাতের পর।"
    )
    med3 = Medication(
        user_id=user.id,
        member_id=mother_member.id,
        brand_name="Seclo 20",
        generic_name="Omeprazole",
        dosage_form="Capsule",
        strength="20mg",
        schedule_pattern="1+0+1",
        meal_timing="খালি পেটে / খাওয়ার ২০ মিনিট আগে (Empty Stomach)",
        morning_time="07:45",
        night_time="20:45",
        start_date=today - datetime.timedelta(days=15),
        end_date=today + datetime.timedelta(days=15),
        is_chronic=False,
        is_active=True,
        doctor_name="Dr. Farhana Yasmin",
        instructions="খাওয়ার ২০-৩০ মিনিট আগে এক গ্লাস পানি দিয়ে গিলতে হবে।"
    )
    med4 = Medication(
        user_id=user.id,
        member_id=self_member.id,
        brand_name="Monas 10",
        generic_name="Montelukast",
        dosage_form="Tablet",
        strength="10mg",
        schedule_pattern="0+0+1",
        meal_timing="রাতে শোবার আগে (At Bedtime)",
        bedtime_time="23:00",
        start_date=today - datetime.timedelta(days=10),
        end_date=today + datetime.timedelta(days=20),
        is_chronic=False,
        is_active=True,
        doctor_name="Dr. Sabrina Rahman",
        instructions="রাতে ঘুমানোর আগে ১টি করে নিয়মিত।"
    )
    db.add_all([med1, med2, med3, med4])
    db.commit()

    # Dose logs for Father's medicines today & past 3 days (to show adherence analytics)
    for delta in range(3, -1, -1):
        log_date = today - datetime.timedelta(days=delta)
        status_morning = "taken"
        status_night = "taken" if delta > 0 else "pending"
        
        # Father Bizoran morning
        db.add(DoseLog(
            medication_id=med1.id,
            user_id=user.id,
            member_id=father_member.id,
            dose_date=log_date,
            slot="morning",
            status=status_morning,
            taken_at=datetime.datetime.combine(log_date, datetime.time(8, 35)) if status_morning == "taken" else None
        ))
        # Father Gluconor morning & night
        db.add(DoseLog(
            medication_id=med2.id,
            user_id=user.id,
            member_id=father_member.id,
            dose_date=log_date,
            slot="morning",
            status=status_morning,
            taken_at=datetime.datetime.combine(log_date, datetime.time(8, 40)) if status_morning == "taken" else None
        ))
        db.add(DoseLog(
            medication_id=med2.id,
            user_id=user.id,
            member_id=father_member.id,
            dose_date=log_date,
            slot="night",
            status=status_night,
            taken_at=datetime.datetime.combine(log_date, datetime.time(21, 45)) if status_night == "taken" else None
        ))

    # Appointments with Chamber & Serial
    doc1 = db.query(Doctor).filter(Doctor.name.like("%Hasan%")).first()
    apt1 = Appointment(
        user_id=user.id,
        member_id=father_member.id,
        doctor_id=doc1.id if doc1 else None,
        doctor_name="Prof. Dr. M. A. Hasan",
        specialty="Medicine & Diabetology",
        chamber_name="Popular Diagnostic Centre, Dhanmondi Branch (Room 304)",
        chamber_address="House 16, Road 2, Dhanmondi, Dhaka",
        appointment_date=today + datetime.timedelta(days=4),
        appointment_time="07:00 PM",
        serial_number="Serial #14 (সিরিয়াল নং ১৪)",
        serial_contact="09613-787801 (Counter Desk)",
        status="Upcoming",
        doctor_advice="Bring latest fasting blood sugar (FBS) and 2HABF report.",
        follow_up_date=today + datetime.timedelta(days=34)
    )
    db.add(apt1)

    # Sample Prescription record
    sample_rx = PrescriptionDocument(
        user_id=user.id,
        member_id=father_member.id,
        title="ডায়াবেটিস ও প্রেসার ফলো-আপ প্রেসক্রিপশন (DMCH File)",
        doctor_name="Prof. Dr. M. A. Hasan",
        hospital_clinic="Popular Diagnostic Centre / DMCH",
        document_date=today - datetime.timedelta(days=60),
        file_path="/static/images/sample_prescription.png",
        file_type="image",
        diagnosis_summary="Type-2 Diabetes Mellitus with Stage-1 Hypertension. Advice: Low salt diet, regular 30 min morning walk."
    )
    db.add(sample_rx)
    db.commit()
    print("Database seeding completed successfully!")
