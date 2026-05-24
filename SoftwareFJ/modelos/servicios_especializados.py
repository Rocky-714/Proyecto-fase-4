from modelos.excepciones import ReservaError


class ServicioBase:

    def __init__(self, costo=0):

        if costo < 0:
            raise ReservaError("El costo no puede ser negativo")

        self.costo = costo

    def calcular_costo(self, horas=1):
        return self.costo * horas


# ================= RESERVA DE SALA =================

class ReservaSala(ServicioBase):

    def __init__(self, costo=0, capacidad=10):

        super().__init__(costo)

        if capacidad <= 0:
            raise ReservaError("Capacidad inválida")

        self.capacidad = capacidad

    def calcular_costo(self, horas=1):

        # Regla: descuento si más de 5 horas
        total = self.costo * horas

        if horas >= 5:
            total *= 0.9  # 10% descuento

        return total


# ================= ALQUILER DE EQUIPO =================

class AlquilerEquipo(ServicioBase):

    def __init__(self, costo=0, estado="disponible"):

        super().__init__(costo)
        self.estado = estado

    def calcular_costo(self, horas=1):

        if self.estado != "disponible":
            raise ReservaError("Equipo no disponible")

        return self.costo * horas


# ================= ASESORÍA ESPECIALIZADA =================

class AsesoriaEspecializada(ServicioBase):

    def __init__(self, costo=0, nivel="basico"):

        super().__init__(costo)
        self.nivel = nivel

    def calcular_costo(self, horas=1):

        # Regla: asesoría siempre mínimo 1 hora
        if horas < 1:
            raise ReservaError("Mínimo 1 hora de asesoría")

        # Nivel avanzado cuesta más
        if self.nivel == "avanzado":
            return self.costo * horas * 1.5

        return self.costo * horas
    