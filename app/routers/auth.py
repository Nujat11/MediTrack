from fastapi import APIRouter, Depends, HTTPException, status, Response, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, FamilyMember
from app.schemas import UserCreate, UserLogin, UserResponse
from app.auth import hash_password, verify_password, create_access_token, get_current_user

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, response: Response, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email.lower()).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="An account with this email already exists.")

    new_user = User(
        name=user_data.name,
        email=user_data.email.lower(),
        phone=user_data.phone,
        hashed_password=hash_password(user_data.password),
        role="user"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Automatically create a default 'Self' family profile
    default_self = FamilyMember(
        user_id=new_user.id,
        name=f"{new_user.name} (Self)",
        relationship="Self",
        emergency_contact=new_user.phone
    )
    db.add(default_self)
    db.commit()

    # Generate token and set auth cookie
    token = create_access_token({"sub": str(new_user.id), "role": new_user.role})
    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        max_age=60 * 60 * 24 * 7,
        samesite="lax"
    )
    return new_user

@router.post("/login")
def login(login_data: UserLogin, response: Response, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == login_data.email.lower()).first()
    if not user or not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password.")

    token = create_access_token({"sub": str(user.id), "role": user.role})
    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        max_age=60 * 60 * 24 * 7,
        samesite="lax"
    )
    return {
        "status": "success",
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }

@router.post("/logout")
@router.get("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"status": "success", "message": "Successfully logged out."}

@router.get("/me", response_model=UserResponse)
def get_current_user_profile(current_user: User = Depends(get_current_user)):
    return current_user
