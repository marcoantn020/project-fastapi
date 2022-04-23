from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.infra.sqlalchemy.config.database import get_database
from src.infra.sqlalchemy.repositories.product_repository import ProductRepository
from src.schemas import schemas

router = APIRouter()


@router.get("/products", response_model=List[schemas.Product])
def list_products(db: Session = Depends(get_database)):
    products = ProductRepository(db).list_all()
    if not len(products):
        raise HTTPException(status_code=204)
    return products


@router.get("/products/{id}", response_model=schemas.Product)
def display_product(id: int, db: Session = Depends(get_database)):
    one_product = ProductRepository(db).list_one(id)
    if not one_product:
        raise HTTPException(status_code=204)
    return one_product


@router.post("/products", status_code=201, response_model=schemas.Product)
def create_product(product: schemas.Product, db: Session = Depends(get_database)):
    created_product = ProductRepository(db).create(product)
    return created_product


@router.put("/products/{id}", response_model=schemas.ProductResponse)
def update_product(id: int, product: schemas.ProductResponse, db: Session = Depends(get_database)):
    ProductRepository(db).update_product(id, product)
    product.id = id
    return product


@router.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_database)):
    ProductRepository(db).delete_product(id)
    return {"message": "Product deleted with success!"}
