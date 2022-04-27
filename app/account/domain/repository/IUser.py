import abc
from ..model.User import User

class IRepository(metaclass=abc.ABCMeta):

   @abc.abstractmethod
   def find(self, id: int) -> User:
      pass
 
   @abc.abstractmethod
   def get_user_by_email(self, email: str) -> User:
      pass

   @abc.abstractmethod
   def create(self, user: User) -> bool:
      pass

   @abc.abstractmethod
   def update(self, user: User) -> bool:
      pass

   @abc.abstractmethod
   def delete(self, id: int) -> bool:
      pass