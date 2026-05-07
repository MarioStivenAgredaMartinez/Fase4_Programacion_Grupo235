# excepciones.py

class ErrorSistema(Exception):
    """Clase base para errores del sistema"""
    pass


class ClienteInvalidoError(ErrorSistema):
    """Error cuando los datos del cliente son inválidos"""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Error cuando el servicio no está disponible"""
    pass


class ReservaError(ErrorSistema):
    """Error relacionado con las reservas"""
    pass


class DuracionInvalidaError(ErrorSistema):
    """Error cuando la duración es incorrecta"""
    pass


class ParametroFaltanteError(ErrorSistema):
    """Error cuando faltan parámetros"""
    pass