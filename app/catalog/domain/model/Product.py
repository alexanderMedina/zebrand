from dataclasses import dataclass
from datetime import datetime

@dataclass()
class Product:
    sku: str
    name: str
    price: float
    brand: str
    id: int = None
    created_at: datetime = str(datetime.utcnow())
    updated_at: datetime = str(datetime.utcnow())

    def dictToObject(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])
        return self