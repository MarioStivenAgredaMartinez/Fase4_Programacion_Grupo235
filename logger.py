# logger.py
# Este módulo se encarga de registrar eventos y errores en un archivo de texto.
# Así se conserva un historial de lo que ocurrió durante la ejecución.

from datetime import datetime
from pathlib import Path


def registrar_evento(tipo: str, mensaje: str) -> None:
    """
    Guarda un evento en el archivo de log.

    Parámetros:
    tipo: tipo de evento, por ejemplo INFO, ERROR o WARNING.
    mensaje: explicación breve del evento ocurrido.
    """

    # Validación básica del tipo de evento.
    if not tipo or not str(tipo).strip():
        tipo = "INFO"

    # Validación básica del mensaje.
    if not mensaje or not str(mensaje).strip():
        mensaje = "Evento sin descripción."

    # Se crea la carpeta logs si todavía no existe.
    carpeta_logs = Path("logs")
    carpeta_logs.mkdir(exist_ok=True)

    # Se define la ruta del archivo donde se guardará la información.
    archivo_log = carpeta_logs / "eventos.log"

    # Se obtiene la fecha y hora actual para registrar cuándo ocurrió el evento.
    fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Se normaliza el tipo de evento para evitar errores en el registro.
    tipo = str(tipo).upper()

    # Se abre el archivo en modo append para no borrar lo anterior.
    with open(archivo_log, "a", encoding="utf-8") as archivo:
        archivo.write(f"[{fecha_hora}] [{tipo}] {mensaje}\n")