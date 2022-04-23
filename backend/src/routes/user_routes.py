from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.config.database import get_database
from src.infra.sqlalchemy.repositories.user_repository import UserRepository
from src.schemas import schemas
from src.infra.providers import hash_provider, token_provider
from src.helpers.auth_helper import get_user_logged

router = APIRouter()


@router.post("/signup", status_code=201, response_model=schemas.UserResponse)
def create_user(user: schemas.User, db: Session = Depends(get_database)):
    user = UserRepository(db).list_by_phone(user.phone)
    if user:
        raise HTTPException(status_code=400, detail="phone already exists in database.")

    user.password = hash_provider.generate_hash(user.password)
    created_user = UserRepository(db).create(user)
    return created_user


@router.post("/signin", response_model=schemas.UserResponseToken)
def login(user: schemas.Login, db: Session = Depends(get_database)):
    phone = user.phone
    password = user.password

    user = UserRepository(db).list_by_phone(phone)
    if user is None:
        raise HTTPException(status_code=400, detail="phone or password incorrect.")

    validat_password = hash_provider.verify_hash(password, user.password)
    if not validat_password:
        raise HTTPException(status_code=400, detail="phone or password incorrect.")

    token = token_provider.create_access_token({'sub': phone})

    return schemas.UserResponseToken(user=user, access_token=token)


@router.get("/me", response_model=schemas.UserResponse)
def me(user: schemas.User = Depends(get_user_logged)):
    return user
