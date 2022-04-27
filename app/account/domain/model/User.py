from dataclasses import dataclass
from datetime import datetime

@dataclass()
class User:
    name: str
    email: str
    password: str
    id: int = None
    admin: bool = True
    created_at: datetime = str(datetime.utcnow())
    updated_at: datetime = str(datetime.utcnow())