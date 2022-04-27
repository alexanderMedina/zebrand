from fastapi import APIRouter, Depends
from app.account.application.dto.UserCreate import UserCreateDto
from app.account.application.dto.UserSignIn import UserSignInDto
from app.account.application.dto.UserUpdate import UserUpdateDto
from app.account.domain.model.User import User
from app.account.domain.repository.IUser import IRepository
from app.account.infraestructure.notification.Email import send_update_email, verify_email_identity
from app.account.infraestructure.repository.User import Repository as repository
from app.account.domain.service.User import Service as service
from app.account.infraestructure.shared.Auth import get_current_user
from app.account.infraestructure.auth import Service as auth
from app.account.application.mapper.User import UserMapper as mapper
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/users/create" , tags=["users"])
async def register(data : UserCreateDto, repository: IRepository = Depends(repository), current_user: User = Depends(get_current_user)):

    if service.get_user_by_email(repository=repository, email=data.email):
        return JSONResponse(status_code=404, content={"detail": "the user already exist"})

    data.password = auth.get_password_hash(data.password)
    user = mapper.fromDtoToDomain(data)
    service.create(repository=repository, user=user)
    verify_email_identity(data.email)

    return JSONResponse(status_code=200, content={"detail": "the user was created"})


@router.post("/users/login", tags=["users"])
def login(data : UserSignInDto, repository: IRepository = Depends(repository)):
    password = data.password
    email = data.email
    response = auth.login(email, password, repository)
    return JSONResponse(status_code=200, content={"detail": response})


@router.put("/users/update", tags=["users"])
def update(data : UserUpdateDto, repository: IRepository = Depends(repository), current_user: User = Depends(get_current_user)):
    
    if data.password:
        data.password = auth.get_password_hash(data.password)

    if not service.find(repository=repository, id=data.id):
        return JSONResponse(status_code=404, content={"detail": "the user does not exist"})
        
    user = mapper.fromDtoToDomain(data)
    service.update(repository=repository, user=user)
    user = mapper.fromDomainToDto(service.find(repository=repository, id=data.id))
    send_update_email(user.email)

    return JSONResponse(status_code=200, content={"detail": "the user was updated"})

@router.delete("/users/{user_id}", tags=["users"])
def delete(user_id: int ,repository: IRepository = Depends(repository), current_user: User = Depends(get_current_user)):

    if not service.find(repository=repository, id=user_id):
        return JSONResponse(status_code=404, content={"detail": "the user does not exist"})

    service.delete(repository=repository, id=user_id)
    return JSONResponse(status_code=200, content={"detail": "the user was deleted"})