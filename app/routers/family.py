from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, FamilyMember
from app.schemas import FamilyMemberCreate, FamilyMemberResponse
from app.auth import get_current_user

router = APIRouter(prefix="/api/family", tags=["Family Profiles"])

@router.get("", response_model=List[FamilyMemberResponse])
def get_family_members(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    members = db.query(FamilyMember).filter(FamilyMember.user_id == current_user.id).all()
    return members

@router.post("", response_model=FamilyMemberResponse)
def add_family_member(
    member_data: FamilyMemberCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    new_member = FamilyMember(
        user_id=current_user.id,
        name=member_data.name,
        relationship=member_data.relationship,
        age=member_data.age,
        gender=member_data.gender,
        blood_group=member_data.blood_group,
        chronic_conditions=member_data.chronic_conditions,
        allergies=member_data.allergies,
        emergency_contact=member_data.emergency_contact
    )
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

@router.put("/{member_id}", response_model=FamilyMemberResponse)
def update_family_member(
    member_id: int,
    member_data: FamilyMemberCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    member = db.query(FamilyMember).filter(
        FamilyMember.id == member_id,
        FamilyMember.user_id == current_user.id
    ).first()
    if not member:
        raise HTTPException(status_code=404, detail="Family member not found.")

    member.name = member_data.name
    member.relationship = member_data.relationship
    member.age = member_data.age
    member.gender = member_data.gender
    member.blood_group = member_data.blood_group
    member.chronic_conditions = member_data.chronic_conditions
    member.allergies = member_data.allergies
    member.emergency_contact = member_data.emergency_contact

    db.commit()
    db.refresh(member)
    return member

@router.delete("/{member_id}")
def delete_family_member(
    member_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    member = db.query(FamilyMember).filter(
        FamilyMember.id == member_id,
        FamilyMember.user_id == current_user.id
    ).first()
    if not member:
        raise HTTPException(status_code=404, detail="Family member not found.")

    db.delete(member)
    db.commit()
    return {"status": "success", "message": "Profile removed successfully."}
