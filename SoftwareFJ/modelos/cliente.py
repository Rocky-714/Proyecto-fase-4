from modelos.entidad import Entidad
from modelos.excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):

        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    # ENCAPSULAMIENTO

    def set_nombre(self, nombre):

        if not nombre or len(nombre.strip()) < 3:
            raise ClienteError("El nombre del cliente es inválido.")

        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_correo(self, correo):

        if "@" not in correo:
            raise ClienteError("Correo electrónico inválido.")

        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def set_telefono(self, telefono):

        if not telefono.isdigit():
            raise ClienteError("El teléfono debe contener solo números.")

        self.__telefono = telefono

    def get_telefono(self):
        return self.__telefono

    # POLIMORFISMO

    def mostrar_informacion(self):

        return (
            f"Cliente: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )