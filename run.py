import sys
import uvicorn

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

if __name__ == "__main__":
    print("=" * 65)
    print(" MediTrack Bangladesh: Web-Based Medication & Treatment Tracker")
    print(" Localized for Bangladeshi Prescription Norms & Caregivers")
    print(" Bilingual Support: Bengali (বাংলা) & English")
    print(" Access application at: http://127.0.0.1:8000")
    print(" Demo User:   demo@meditrack.bd   | Password: password123")
    print(" Admin User:  admin@meditrack.bd  | Password: admin123")
    print("=" * 65)
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
