from pydantic import BaseModel, EmailStr, constr

class UserDto(BaseModel):
    id: int
    name: constr(min_length=3) = None
    email: EmailStr = None
    password: constr(min_length=6) = None