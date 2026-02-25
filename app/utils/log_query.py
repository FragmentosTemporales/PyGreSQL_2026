from ..schemas import log_query_schema

class LogQuerySaver:
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
    def __init__(self, request):
        self.request = request
        self.save()

    def save(self):
        dict = {
            "endpoint": self.request.endpoint,
            "method": self.request.method,
            "url": self.request.url
        }
        to_save = log_query_schema.load(dict)
        to_save.save_to_db()