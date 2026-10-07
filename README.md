# MediTrack

MediTrack is a web-based medication and treatment tracking system designed for patients, caregivers, and families to manage health records more efficiently. It supports medication schedules, appointment tracking, doctor management, prescription documents, and family health monitoring in a simple and user-friendly dashboard.

## Overview

MediTrack helps users keep track of:

- Medicines and dosage schedules
- Family member health profiles
- Upcoming appointments and visits
- Doctor information and consultation details
- Prescription uploads and document records
- Daily medication adherence and health routines

The application is built with FastAPI and uses a database-backed backend to manage patient and caregiver information securely.

## Key Features

- Family member management for individual health tracking
- Medication logs with dosage, timing, and reminders
- Appointment scheduling and status tracking
- Doctor directory with specialty and chamber details
- Prescription document upload and storage
- User authentication and dashboard access
- Admin support for viewing and managing records
- Responsive web interface for desktop and mobile usage

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- Jinja2 Templates
- SQLite
- HTML, CSS, and JavaScript

## Project Structure

```text
MediTrack/
├── app/
│   ├── routers/
│   ├── static/
│   ├── UI/
│   ├── auth.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── seed_data.py
├── requirements.txt
├── run.py
├── test_endpoints.py
├── README.md
└── app.db
```

## Getting Started

### 1. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn app.main:app --reload
```

Then open the app in your browser at:

```text
http://localhost:8000
```

## Running the App via Script

You may also run the project using the included script:

```bash
python run.py
```
