from abc import ABC, abstractmethod

class Entidad(ABC):

    @abstractmethod
    def mostrar_informacion(self):
        pass