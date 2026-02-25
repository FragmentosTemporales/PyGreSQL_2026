from ..schemas import log_error_schema

class LogErrorSaver:
    """
    Registra automáticamente las consultas HTTP recibidas en la aplicación web.
    
    Esta clase captura información sobre las solicitudes HTTP (endpoint, método, URL)
    y las almacena en la base de datos para auditoría y análisis. Las solicitudes
    provenientes del entorno local (127.0.0.1:5050) se excluyen del registro para
    evitar ruido durante el desarrollo.
    
    Args:
        request: Objeto de solicitud Flask que contiene la información de la petición HTTP
        
    Example:
        # El log se guarda automáticamente al instanciar la clase
        log_saver = LogQuerySaver(request)
    """
    def __init__(self, function_name, error_message):
        self.function_name = function_name
        self.error_message = error_message
        self.save()

    def save(self):
        dict = {
            "function_name": self.function_name,
            "error_message": self.error_message,
        }
        to_save = log_error_schema.load(dict)
        to_save.save_to_db()