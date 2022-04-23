from sqlalchemy.orm import Session
from sqlalchemy import select
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class OrderRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, order: schemas.Order):
        create_order = models.Order(
            amount=order.amount,
            delivery_place=order.delivery_place,
            observation=order.observation,
            delivery_type=order.delivery_type,
            user_id=order.user_id,
            product_id=order.product_id
        )

        self.db.add(create_order)
        self.db.commit()
        self.db.refresh(create_order)
        return create_order

    def list_all(self):
        order_stmt = select(models.Order)
        order_stmt = self.db.execute(order_stmt).scalars().all()
        return order_stmt

    def list_one(self, id: int):
        order_stmt = select(models.Order).where(models.Order.id == id)
        order_stmt = self.db.execute(order_stmt).scalars().first()
        return order_stmt

    def list_my_orders_by_user_id(self, user_id: int):
        order_stmt = select(models.Order).where(models.Order.user_id == user_id)
        order_stmt = self.db.execute(order_stmt).scalars().all()
        return order_stmt

    def list_my_shopping_by_user_id(self, user_id: int):
        order_stmt = select(models.Order, models.Product)\
            .join_from(models.Order, models.Product)\
            .where(models.Product.user_id == user_id)
        order_stmt = self.db.execute(order_stmt).scalars().all()
        return order_stmt

    def delete(self):
        pass
