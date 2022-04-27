from ..repository.IUser import IRepository
from ..model.User import User

class Service():
   
    def create(repository: IRepository, user: User) -> bool:
        response = repository.create(user=user)
        return response

    def update(repository: IRepository, user: User) -> bool:
        response = repository.update(user=user)
        return response
        
    def delete(repository: IRepository, id: int) -> bool:
        response = repository.delete(id=id)
        return response

    def get_user_by_email(repository: IRepository, email: str) -> User:
        response = repository.get_user_by_email(email=email)
        return response

    def find(repository: IRepository, id: int) -> User:
        response = repository.find(id=id)
        return response
        
