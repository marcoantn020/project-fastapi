from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class ProductRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        create_product = models.Product(
            name=product.name,
            details=product.details,
            price=product.price,
            available=product.available,
            user_id=product.user_id
        )

        self.db.add(create_product)
        self.db.commit()
        self.db.refresh(create_product)
        return create_product

    def list_all(self):
        products = self.db.query(models.Product).all()
        return products

    def list_one(self, id: int):
        product_stmt = select(models.Product).where(models.Product.id == id)
        product_stmt = self.db.execute(product_stmt).scalars().first()
        return product_stmt

    def update_product(self, id: int, product: schemas.ProductResponse):
        update_stmt = update(models.Product).where(models.Product.id == id).values(
            name=product.name,
            details=product.details,
            price=product.price,
            available=product.available
        )

        self.db.execute(update_stmt)
        self.db.commit()

    def delete_product(self, id: int):
        delete_stmt = delete(models.Product).where(models.Product.id == id)
        self.db.execute(delete_stmt)
        self.db.commit()
