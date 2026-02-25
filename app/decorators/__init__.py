
import time
from rich import print


def time_decorator(base_func : callable = None):
    def exec_func(*args, **kwargs):
        start_time = time.time()
        try:
            result = base_func(*args, **kwargs)
        except Exception as e:
            raise e
        end_time = time.time()
        exec_time = end_time - start_time
        print(f"[bold green]Función '{base_func.__name__}' ejecutada en {exec_time:.4f} segundos.[/bold green]")
        return result
    return exec_func

def log_decorator(base_func : callable = None):
    def exec_func(*args, **kwargs):
        print(f"[bold blue]Iniciando función '{base_func.__name__}'...[/bold blue]")
        result = base_func(*args, **kwargs)
        print(f"[bold blue]Función '{base_func.__name__}' finalizada.[/bold blue]")
        return result
    return exec_func

def retry_decorator(base_func : callable = None):
    def exec_func(*args, **kwargs):
        max_retries = 9
        for attempt in range(1, max_retries + 1):
            try:
                return base_func(*args, **kwargs)
            except Exception as e:
                print(f"[bold red]Error en intento {attempt} de '{base_func.__name__}': {e}[/bold red]")
                if attempt == max_retries:
                    print(f"[bold red]Máximo de reintentos alcanzado para '{base_func.__name__}'.[/bold red]")
                    raise
                time.sleep(1)
    return exec_func
