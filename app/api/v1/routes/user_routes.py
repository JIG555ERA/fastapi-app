from fastapi import APIRouter
from app.controllers.user_controller import ( get_users, create_user )

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get('/')
def fetch_users():
    return get_users()

@router.post('/')
def add_user(name: str):
    return create_user(name)
