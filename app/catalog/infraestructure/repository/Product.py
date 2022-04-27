from dataclasses import asdict
from fastapi import Depends
import os
from app.catalog.domain.repository.IProduct import IRepository
from app.catalog.domain.model.Product import Product
from database.models import get_db
from sqlalchemy.orm import Session

class Repository(IRepository):

    def __init__(self, session : Session = Depends(get_db)):
        self.session = session

    def list(self, page: int) -> list:
        catalog = self.session.query(Product).slice( (page - 1) * int(os.getenv('PER_PAGE')), int(os.getenv('PER_PAGE'))).all()
        return catalog

    def total(self) -> int:
        total_number = self.session.query(Product).count()
        return total_number

    def find(self, id: int) -> Product:
        product = self.session.query(Product).filter(Product.id == id).first()
        return product

    def find_by_sku(self, sku: str) -> Product:
        product = self.session.query(Product).filter(Product.sku == sku).first()
        return product

    def create(self, product: Product) -> bool:
        response = self.session.add(product)
        self.session.commit()
        return response

    def update(self, product: Product) -> bool:
        productDict = {k:v for k, v in asdict(product).items() if v is not None}
        productDict.pop('created_at')
        response = self.session.query(Product).filter(Product.id == product.id).update(productDict, synchronize_session="fetch")
        self.session.commit()
        return response

    def delete(self, id: int) -> bool:
        deleted = self.session.query(Product).filter(Product.id == id).delete(synchronize_session="fetch")
        self.session.commit()
        return deleted
