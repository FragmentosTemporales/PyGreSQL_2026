from flask import Flask
from app.routes import base_route, producto_route, auth_route
from rich import print
from app.config import config, s
from app.models import db, migrate
from flasgger import Swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity



def create_app(test_mode=False):
    try:
        app = Flask(__name__, instance_relative_config=True)

        jwt = JWTManager()
        cors = CORS(resources={r"/*": {"origins": "*"}})

        if test_mode:
            print("[bold yellow] Starting app in test mode [/bold yellow]")
            app.config.from_object(config["test"])

        else:
            print("[bold green] Starting app in development mode [/bold green]")
            env = s.flask_env
            app.config.from_object(config[env])


        swagger = Swagger(app, template={
            "swagger": "2.0",
            "info": {
                "title": "PyGreSQL API",
                "description": "API for PyGreSQL",
                "version": "1.0.0"
            },
            "tags": [
                {
                    "name": "Auth",
                    "description": "Authentication related endpoints"
                },
                {
                    "name": "Base",
                    "description": "Base endpoints"
                },
                {
                    "name": "Producto",
                    "description": "Endpoints related to products"
                }
            ]
        })

        db.init_app(app)
        migrate.init_app(app, db)
        cors.init_app(app)
        jwt.init_app(app)

        app.register_blueprint(auth_route)
        app.register_blueprint(base_route)
        app.register_blueprint(producto_route)

        @app.errorhandler(404)
        def page_not_found(error):
            return "404 Not Found", 404

        return app

    except Exception as e:
        print(f"[bold red] Error creating app: {e} [/bold red]")
