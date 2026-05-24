from abc import ABC, abstractmethod
from modelos.entidad import Entidad


class Servicio(Entidad, ABC):

    def __init__(self, nombre, precio_base):

        self.set_nombre(nombre)
        self.set_precio_base(precio_base)

    # ENCAPSULAMIENTO

    def set_nombre(self, nombre):

        if not nombre or len(nombre.strip()) < 3:
            raise ValueError("Nombre del servicio inválido.")

        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_precio_base(self, precio):

        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")

        self.__precio_base = precio

    def get_precio_base(self):
        return self.__precio_base

    # MÉTODOS ABSTRACTOS

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    # POLIMORFISMO

    def mostrar_informacion(self):

        return (
            f"Servicio: {self.__nombre} | "
            f"Precio Base: ${self.__precio_base}"
        )