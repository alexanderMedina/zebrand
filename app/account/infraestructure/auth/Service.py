
import os
from app.account.domain.repository.IUser import IRepository
from .Jwt import pwd_context, oauth2_scheme, TokenData
from app.account.domain.model.User import User
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from typing import Optional
from ..repository.User import Repository
from app.account.infraestructure.repository.User import Repository as repository

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(email: str, password: str, repository: IRepository) -> User or bool:
    
    user = repository.get_user_by_email(email=email)

    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY") , algorithm=os.getenv("ALGORITHM"))
    
    return encoded_jwt

def login(email: str, password: str, repository: IRepository):

    user = authenticate_user(email, password, repository)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}