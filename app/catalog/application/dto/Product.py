from pydantic import BaseModel, constr

class ProductDTO(BaseModel):
    id: int
    sku: constr(min_length=8)
    name: constr(min_length=3)
    price: float
    brand: constr(min_length=2)