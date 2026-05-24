from modelos.cliente import Cliente
from modelos.reserva import Reserva
from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from modelos.excepciones import ClienteError, ReservaError
from utils.logger import registrar_log


def ejecutar_simulaciones():

    salida = []

    def log(msg):
        registrar_log(msg)
        salida.append(msg)

    log("INICIO SIMULACIONES")

    # Cliente válido (CORREGIDO)
    try:
        c1 = Cliente("Juan", "juan@test.com", "300111")
        log("Cliente válido creado")
    except ClienteError as e:
        log(f"ERROR cliente válido: {e}")
        c1 = None

    # Cliente inválido controlado
    try:
        Cliente("", "456", "")
    except ClienteError as e:
        log(f"ERROR cliente inválido controlado: {e}")

    # Servicios
    s1 = ReservaSala(); s1.costo = 100
    s2 = AlquilerEquipo(); s2.costo = 50
    s3 = AsesoriaEspecializada(); s3.costo = 200

    log("Servicios creados")

    # Reserva válida
    try:
        if not c1:
            raise ReservaError("Cliente no creado")

        r1 = Reserva(c1, s1)
        r1.total = s1.costo * 2
        log("Reserva válida creada")

    except ReservaError as e:
        log(f"ERROR reserva válida: {e}")

    # Reserva inválida
    try:
        Reserva(None, s2)
    except Exception as e:
        log(f"ERROR reserva inválida controlado: {e}")

    # Error costo
    try:
        s4 = ReservaSala()
        s4.costo = -10
        if s4.costo < 0:
            raise ValueError("Costo inválido")
    except Exception as e:
        log(f"ERROR costo controlado: {e}")

    log("FIN SIMULACIONES")

    return "\n".join(salida)
