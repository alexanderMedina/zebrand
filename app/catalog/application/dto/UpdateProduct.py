from pydantic import BaseModel, constr

class ProductUpdateDTO(BaseModel):
    id: int
    sku: constr(min_length=8) = None
    name: constr(min_length=3) = None
    price: float = None
    brand: constr(min_length=2) = None
   