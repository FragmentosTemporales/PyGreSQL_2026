from flask import Blueprint
from app.models import Producto
from app.schemas import producto_schema, productos_schema, log_error_schema
from flask import jsonify, request
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required
)
from rich import print
from ..utils import LogQuerySaver, LogErrorSaver

producto_route = Blueprint('producto', __name__)

@producto_route.route('/GET/productos', methods=['GET'])
def get_productos():
    """
    Docstring for get_productos
    ---    
    tags:
      - Producto
    responses:
      200:
        description: A list of productos
      500:
        description: Internal Server Error
    """
    LogQuerySaver(request)
    try:
        productos = Producto.get_all()
        return jsonify(productos_schema.dump(productos)), 200

    except Exception as e:
        LogErrorSaver(error_message=str(e), function_name="get_productos")
        return jsonify({"error": "Error interno en el Servidor", "message": str(e)}), 500


@producto_route.route('/POST/producto', methods=['POST'])
# @jwt_required()
def create_producto():
    """
    Docstring for create_producto
    ---
    tags:
      - Producto
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nombre
            - codigo
            - marca
            - valor
          properties:
            nombre:
              type: string
              description: Nombre del producto
              example: "Producto de prueba"
            codigo:
              type: string
              description: Código único del producto
              example: "123321654983"
            marca:
              type: string
              description: Marca del producto
              example: "Marca de prueba"
            valor:
              type: number
              description: Valor del producto
              example: 100
    responses:
      201:
        description: Producto created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              description: ID del producto creado
            nombre:
              type: string
              description: Nombre del producto
            codigo:
              type: string
              description: Código único del producto
            marca:
              type: string
              description: Marca del producto
            valor:
              type: number
              description: Valor del producto
          example:
            id: 1
            nombre: "Producto de prueba"
            codigo: "123321654983"
            marca: "Marca de prueba"
            valor: 100
      400:
        description: Bad Request
        schema:
          type: object
          properties:
            error:
              type: string
              example: "El código ya existe en la base de datos."
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

        try:
            producto = producto_schema.load(args_json)
        except ValueError as ve:
            if "El código ya existe en la base de datos." in str(ve):
                producto_existente = Producto.get_producto_by_codigo(args_json["codigo"])
                if producto_existente:
                    res = {
                        "error": "El código ya existe en la base de datos.",
                        "producto_existente": producto_schema.dump(producto_existente)
                    }
                    return jsonify(res), 400

            return jsonify({"error": str(ve)}), 400

        producto.save_to_db()

        return jsonify(producto_schema.dump(producto)), 201

    except Exception as e:
        LogErrorSaver(error_message=str(e), function_name="create_producto")
        return jsonify({"error": str(e)}), 500
