from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.config.database import get_database
from src.infra.sqlalchemy.repositories.order_repository import OrderRepository
from src.schemas import schemas
from src.helpers.auth_helper import get_user_logged

router = APIRouter()


@router.get("/orders", response_model=List[schemas.Order])
def list_orders(db: Session = Depends(get_database)):
    orders = OrderRepository(db).list_all()
    if not len(orders):
        raise HTTPException(status_code=204)
    return orders


@router.get("/orders/my_orders", response_model=List[schemas.Order])
def list_my_orders(user: schemas.UserAutenticad = Depends(get_user_logged), db: Session = Depends(get_database)):
    try:
        orders = OrderRepository(db).list_my_orders_by_user_id(user.id)
    except:
        raise HTTPException(status_code=204)
    else:
        return orders


@router.get("/orders/my_shopping", response_model=List[schemas.Order])
def list_my_shopping(user: schemas.UserAutenticad = Depends(get_user_logged), db: Session = Depends(get_database)):
    try:
        orders = OrderRepository(db).list_my_shopping_by_user_id(user.id)
    except Exception as e:
        return e
    else:
        if not len(orders):
            raise HTTPException(status_code=204)
        return orders


@router.post("/orders", status_code=201, response_model=schemas.Order)
def create_orders(order: schemas.Order, db: Session = Depends(get_database)):
    created_order = OrderRepository(db).create(order)
    return created_order
