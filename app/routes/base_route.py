from flask import Blueprint, jsonify, request
from ..utils import LogQuerySaver, LogErrorSaver

base_route = Blueprint('base', __name__)

@base_route.route('/')
def index():
    """
    Docstring for the base route endpoint.
    ---
    tags:
      - Base

    responses:
      200:
        description: Consulta Exitosa

      500:
        description: Error Interno del Servidor
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Error Interno del Servidor"
    """
    LogQuerySaver(request)
    try:

        return jsonify({"message": "Welcome to the PyGreSQL API!"}), 200

    except Exception as e:
        LogErrorSaver(error_message=str(e), function_name="index")
        return jsonify({"error": "Error interno del servidor"}), 500