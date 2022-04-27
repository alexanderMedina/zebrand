from dataclasses import asdict
from fastapi import Depends
from app.account.domain.repository.IUser import IRepository
from app.account.domain.model.User import User
from database.models import get_db
from sqlalchemy.orm import Session

class Repository(IRepository):

    def __init__(self, session : Session = Depends(get_db)):
        self.session = session

    def find(self, id: id) -> User:
        user = self.session.query(User).filter(User.id == id).first()
        return user

    def get_user_by_email(self, email: str) -> User:
        user = self.session.query(User).filter(User.email == email).first()
        return user

    def create(self, user: User) -> bool:
        response = self.session.add(user)
        self.session.commit()
        return response

    def update(self, user: User) -> bool:
        userDict = {k:v for k, v in asdict(user).items() if v is not None}
        userDict.pop('created_at')
        response = self.session.query(User).filter(User.id == user.id).update(userDict, synchronize_session="fetch")
        self.session.commit()
        return response

    def delete(self, id: int) -> bool:
        deleted = self.session.query(User).filter(User.id == id).delete(synchronize_session="fetch")
        self.session.commit()
        return deleted

