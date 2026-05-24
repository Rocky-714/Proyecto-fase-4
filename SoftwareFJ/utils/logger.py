from datetime import datetime

LOG_FILE = "registro.log"


def registrar_log(mensaje, tipo="INFO"):
    """
    Registra eventos del sistema en un archivo log
    """

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linea = f"[{tipo}] {fecha} - {mensaje}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(linea)
         