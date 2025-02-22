from src.model.entities.eventos import Eventos
from abc import ABC, abstractclassmethod

class EventosRepositoryInterface(ABC):
    @abstractclassmethod
    def insert(self, event_name:str) -> None:
        pass
            

    @abstractclassmethod
    def select_event(self, event_name:str) -> Eventos :
        pass
