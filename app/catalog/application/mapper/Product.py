from typing import List
from pydantic import parse_obj_as
from app.catalog.application.dto.Product import ProductDTO
from app.catalog.domain.model.Product import Product

class ProductMapper():

    def fromDomainToDto(product: Product):
        
        product = ProductDTO(
            id=product.id, 
            brand=product.brand, 
            name=product.name, 
            price=product.price, 
            sku=product.sku, 
            created_at=product.created_at
        )

        return product

    def fromDtoToDomain(product: ProductDTO):
        product_dict = product.dict()
        product = Product(**product_dict)
        return product
    
    def fromDomainListToDtoList(products: list):
        catalogs_dict = [product.__dict__ for product in products]
        catalog = parse_obj_as(List[ProductDTO], catalogs_dict)
        return catalog