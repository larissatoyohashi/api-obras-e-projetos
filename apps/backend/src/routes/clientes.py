from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Cliente
from ..schemas.cliente_schema import ClienteSchema
from pydantic import ValidationError

clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')

@clientes_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo Cliente
    ---
    tags:
      - Clientes
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Cliente'
    responses:
      201:
        description: Cliente criado com sucesso
        schema:
          $ref: '#/definitions/Cliente'
    """
    try:
        data = ClienteSchema(**request.json)
        novo_cliente = Cliente(**data.model_dump(exclude_none=True))
        db.session.add(novo_cliente)
        db.session.commit()
        
        return jsonify(novo_cliente.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@clientes_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os clientes
    ---
    tags:
      - Clientes
    responses:
      200:
        description: OK
    """
    clientes = Cliente.query.all()
    result = [ClienteSchema(**c.to_dict()).model_dump() for c in clientes]
    return jsonify(result), 200

@clientes_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um cliente específico pelo ID
    ---
    tags:
      - Clientes
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro
    responses:
      200:
        description: OK
    """
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    
    return jsonify(cliente.to_dict()), 200

@clientes_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um cliente existente
    ---
    tags:
      - Clientes
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Cliente'
    responses:
      200:
        description: OK
    """
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    try:
        data = request.json
        
        cliente.nome = data.get('nome', cliente.nome)
        cliente.cpf = data.get('cpf', cliente.cpf)
        cliente.telefone = data.get('telefone', cliente.telefone)
        
        db.session.commit()
        return jsonify(cliente.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@clientes_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um cliente
    ---
    tags:
      - Clientes
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do registro a ser removido
    responses:
      200:
        description: OK
      404:
        description: Não encontrado
    """  
    cliente = Cliente.query.get(id)

    if not cliente:
        return jsonify({"error": "Cliente não encontrado"}), 404
    
    db.session.delete(cliente)
    db.session.commit()

    return jsonify({"mensagem": "Cliente removido com sucesso"}), 200