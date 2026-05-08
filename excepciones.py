# excepciones.py
# En este archivo se definen las excepciones personalizadas del sistema.
# Estas excepciones ayudan a identificar errores específicos de forma clara.


class ErrorAplicacion(Exception):
    """Excepción base para todos los errores del sistema."""

    def __init__(self, mensaje="Ha ocurrido un error en la aplicación."):
        super().__init__(mensaje)


class ClienteInvalidoError(ErrorAplicacion):
    """Se genera cuando un cliente tiene datos inválidos."""

    def __init__(self, mensaje="Los datos del cliente no son válidos."):
        super().__init__(mensaje)


class ServicioNoValidoError(ErrorAplicacion):
    """Se genera cuando un servicio tiene información incorrecta."""

    def __init__(self, mensaje="La información del servicio es inválida."):
        super().__init__(mensaje)


class ServicioNoDisponibleError(ErrorAplicacion):
    """Se genera cuando se intenta usar un servicio no disponible."""

    def __init__(self, mensaje="El servicio no se encuentra disponible."):
        super().__init__(mensaje)


class ReservaError(ErrorAplicacion):
    """Se genera cuando ocurre un problema al crear, procesar o cancelar una reserva."""

    def __init__(self, mensaje="Ha ocurrido un error en la reserva."):
        super().__init__(mensaje)