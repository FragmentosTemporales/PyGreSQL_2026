from flask import Blueprint, jsonify, request, render_template
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
    create_access_token
)
from ..models import Usuario
from ..schemas import *
from ..utils import LogQuerySaver, LogErrorSaver

auth_route = Blueprint('auth', __name__)


@auth_route.route("/login", methods=["POST"])
def login_user():
    """
    Docstring for login_user
    ---
    tags:
      - Auth
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - correo
            - clave
          properties:
            correo:
              type: string
              description: User email
              example: "correo.prueba@mail.com"
            clave:
              type: string
              description: User password
              example: "12345678"
    responses:
      200:
        description: Successful Login
        schema:
          type: object
          properties:
            usuario:
              type: object
              description: User information
            token:
              type: string
              description: JWT access token
          example:
            usuario: {
              "apellido": "Rivera",
              "correo": "correo.prueba@mail.com",
              "fecha_registro": "2026-02-18T02:50:20.587778",
              "id": 3,
              "nombre": "Cristian"
              }
            token: "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
      400:
        description: Bad Request
        schema:
          type: object
          properties:
            error:
              type: string
              example: "ERROR DE USUARIO O CONTRASEÑA"
      500:
        description: Internal Server Error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Internal Server Error"
    """
    LogQuerySaver(request)
    try:
        args_json = request.get_json()
        args = login_schema.load(args_json)

        correo = args["correo"]
        clave = args["clave"]

        usuario = Usuario.find_by_correo(correo)

        if not usuario or not Usuario.verify_password(clave, usuario.clave):
            return jsonify({"error": "Error de usuario o contraseña"}), 400

        access_token = create_access_token(correo)
        usuario = usuario_schema.dump(usuario)

        return jsonify(
            {   "usuario": usuario,
                "token": access_token,
            }
        ), 200

    except Exception as e:
        LogErrorSaver(error_message=str(e), function_name="login_user")
        return jsonify({"error": "Error interno en el Servidor", "message": str(e)}), 500
