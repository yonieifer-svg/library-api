from fastapi import APIRouter
from database.member_db import member_repo 

router = APIRouter()

@router.post("")
def create_member(data: dict):
    return member_repo.create_member(data)

@router.get("")
def get_all_members():
    return member_repo.get_all_members()

@router.get("/{id}")
def get_member_by_id(id: int):
    return member_repo.get_member_by_id(id)

@router.patch("/{id}")
def update_member(id: int, data: dict):
    return member_repo.update_member(id, data)

@router.patch("/{id}/deactivate")
def deactive_member(id: int):
    return member_repo.deactive_member(id)

@router.patch("/{id}/activate")
def active_member(id: int):
    return member_repo.active_member(id)
