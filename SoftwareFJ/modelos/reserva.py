from datetime import datetime
from modelos.excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, horas=1):

        # VALIDACIONES BÁSICAS
        if cliente is None:
            raise ReservaError("Cliente inválido")

        if servicio is None:
            raise ReservaError("Servicio inválido")

        if horas <= 0:
            raise ReservaError("Las horas deben ser mayores a 0")

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas

        # Cálculo automático del costo
        self.total = self.calcular_total()

        # Metadata
        self.fecha = datetime.now()

    # ================= LÓGICA DE NEGOCIO =================

    def calcular_total(self):

        costo_base = getattr(self.servicio, "costo", None)

        if costo_base is None:
            raise ReservaError("El servicio no tiene costo definido")

        return costo_base * self.horas

    # ================= REPRESENTACIÓN =================

    def __str__(self):

        return (
            f"Reserva:\n"
            f"- Cliente: {self.cliente.nombre}\n"
            f"- Servicio: {type(self.servicio).__name__}\n"
            f"- Horas: {self.horas}\n"
            f"- Total: {self.total}\n"
            f"- Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}"
        )
    