import abc
from xmlrpc.client import Boolean
from ..model.Product import Product

class IRepository(metaclass=abc.ABCMeta):
 
   @abc.abstractmethod
   def list(self, page) -> list:
      pass

   @abc.abstractmethod
   def create(self, product: Product) -> Product:
      pass

   @abc.abstractmethod
   def delete(self, id: int) -> bool:
      pass

   @abc.abstractmethod
   def find(self, id: int) -> Product:
      pass

   @abc.abstractmethod
   def total(self) -> int:
      pass

   @abc.abstractmethod
   def find_by_sku(self, sku: str) -> Product:
      pass

   @abc.abstractmethod
   def update(self, product: Product) -> bool:
      pass