from src.model.entities.inscritos import Inscritos
from abc import ABC, abstractclassmethod


class SubscribersRepositoryInterface(ABC):
    @abstractclassmethod
    def insert(self, subscriber_infos:dict) -> None:
        pass    


    @abstractclassmethod
    def select_subscriber(self,email:str, evento_id:int) -> Inscritos:
        pass