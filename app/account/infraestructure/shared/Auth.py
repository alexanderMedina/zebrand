
import os
from app.account.domain.repository.IUser import IRepository
from ..auth.Jwt import pwd_context, oauth2_scheme, TokenData
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from app.account.infraestructure.repository.User import Repository as repository


def get_current_user(repository: IRepository = Depends(repository), token: str = Depends(oauth2_scheme), ):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("ALGORITHM")])
        email: str = payload.get("sub")
       
        if email is None:
            raise credentials_exception
        
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = repository.get_user_by_email(email=token_data.email)
    
    if user is None:
        raise credentials_exception
    
    return user