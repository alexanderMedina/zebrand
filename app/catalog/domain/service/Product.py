from ..repository.IProduct import IRepository
from ..model.Product import Product

class ProductService():
   
    def create(repository: IRepository, product: Product) -> bool:
        response = repository.create(product=product)
        return response
        
    def list(repository: IRepository, page: int) -> list:
        response = repository.list(page=page)
        return response

    def find(repository: IRepository, id: int) -> Product:
        response = repository.find(id=id)
        return response

    def total(repository: IRepository) -> int:
        response = repository.total()
        return response

    def find_by_sku(repository: IRepository, sku: str) -> Product:
        response = repository.find_by_sku(sku=sku)
        return response
        
    def delete(repository: IRepository, id: int) -> bool:
        response = repository.delete(id=id)
        return response
        
    def update(repository: IRepository, product: Product) -> bool:
        response = repository.update(product=product)
        return response
        
