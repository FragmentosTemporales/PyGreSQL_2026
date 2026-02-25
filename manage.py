from app import create_app
from rich import print
from flask.cli import FlaskGroup
from app.models import Usuario


cli = FlaskGroup(create_app=create_app)


def main():
    print("[bold green]Iniciando la aplicación...[/bold green]")
    cli()


# python manage.py exec
@cli.command("exec")
def exec():
    try:
        from app.schemas import usuario_schema
        print("[bold green]Iniciando el ejecutor...[/bold green]")
        usuario_dict = {
            "nombre": "Cristian",
            "apellido": "Rivera",
            "correo": "correo.prueba@mail.com",
            "clave": "12345678" 
        }

        usuario : Usuario = None

        usuario = usuario_schema.load(usuario_dict)
        usuario.clave = usuario.hash_password(usuario.clave)

        try:
            usuario.validate_correo_structure(usuario.correo)
        except ValueError as ve:
            print(f"[bold red]Error de validación: {ve}[/bold red]")
            return

        print("[bold green]Usuario cargado desde el diccionario:[/bold green]")

        usuario.save_to_db()

        print("[bold green]Usuario guardado en la base de datos:[/bold green]")

        print(usuario_schema.dump(usuario))

    except Exception as e:
        print(f"[bold red]Error al ejecutar el comando 'exec': {e}[/bold red]")


@cli.command("delete")
def delete():
    try:
        print("[bold green]Eliminando todos los usuarios...[/bold green]")
        usuario : Usuario = Usuario.find_by_id(2)
        usuario.delete_from_db()
        print("[bold green]Usuarios eliminados de la base de datos.[/bold green]")
    except Exception as e:
        print(f"[bold red]Error al eliminar usuarios: {e}[/bold red]")


if __name__ == "__main__":

    main()
