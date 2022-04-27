from pydantic import BaseModel, constr

class ProductCreateDTO(BaseModel):
    sku: constr(min_length=8)
    name: constr(min_length=3)
    price: float
    brand: constr(min_length=2)
   