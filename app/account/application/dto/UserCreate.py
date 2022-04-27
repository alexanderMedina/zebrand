from pydantic import BaseModel, EmailStr, constr

class UserCreateDto(BaseModel):
    name: constr(min_length=3)
    email:EmailStr
    password: constr(min_length=6)