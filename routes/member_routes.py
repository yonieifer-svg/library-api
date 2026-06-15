from fastapi import APIRouter, HTTPException
from database.member_db import member_repo 
from schema import CreateMember, UpdateMember

router = APIRouter()

@router.post("")
def create_member(data: CreateMember):
    email_already_used = member_repo.find({"email": data["email"]})
    if email_already_used:
        raise HTTPException(400, "email")
    return member_repo.create_member(data)

@router.get("")
def get_all_members():
    return member_repo.get_all_members()

@router.get("/{id}")
def get_member_by_id(id: int):
    return member_repo.get_member_by_id(id)

@router.patch("/{id}")
def update_member(id: int, data: UpdateMember):
    return member_repo.update_member(id, data)

@router.patch("/{id}/deactivate")
def deactive_member(id: int):
    return member_repo.deactive_member(id)

@router.patch("/{id}/activate")
def active_member(id: int):
    return member_repo.active_member(id)
