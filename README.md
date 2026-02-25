# PYTHON/POSTGRESQL 2026 #

## APLICACIÓN DE PRUEBA PARA CONECTAR APLICACION FLASK Y POSTGRESQL ##

## 📥 Instalación ##

1.- Crear base de datos en Postgresql

>> CREATE DATABASE dbpygresql;

2.- Crear entorno virtual

>> python -m venv venv

3.- Activar entorno virtual

>> source venv/scripts/activate

4.- Instalar dependencias

>> pip install -r requirements.txt

### .✨ Iniciar base de datos ##

1.- Para iniciar migraciones

>> python manage.py db init

2.- Para migrar modelos a base de datos

>> python manage.py db migrate

3.- Para actualizar base de datos

>> python manage.py db upgrade

### 🤖 Ejecución ###

1.- Para iniciar la aplicación

>> flask run --host=0.0.0.0 --port=5050

2.- Crear usuario de prueba

>> python manage.py exec

## 😎 Creado por ##

```bash
Cristian Rivera Acevedo
cristian.rivera3284@gmail.com
+56963410066
```
