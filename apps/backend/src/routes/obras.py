from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Obra
from ..schemas.obra_schema import ObraSchema
from pydantic import ValidationError

obras_bp = Blueprint('obras', __name__, url_prefix='/obras')

@obras_bp.route('/', methods=['POST'])
def create():
    """
    Criar uma nova Obra
    ---
    tags:
      - Obras
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Obra'
    responses:
      201:
        description: Obra criada com sucesso
        schema:
          $ref: '#/definitions/Obra'
    """
    try:
        data = ObraSchema(**request.json)
        nova_obra = Obra(**data.model_dump(exclude_none=True))
        db.session.add(nova_obra)
        db.session.commit()
        
        return jsonify(nova_obra.to_dict()), 201
    except ValidationError as err:
        return jsonify({"errors": err.errors()}), 400

@obras_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todas as obras
    ---
    tags:
      - Obras
    responses:
      200:
        description: OK
    """
    obras = Obra.query.all()
    result = [ObraSchema(**o.to_dict()).model_dump() for o in obras]
    return jsonify(result), 200

@obras_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista uma obra específica pelo ID
    ---
    tags:
      - Obras
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
    obra = Obra.query.get(id)

    if not obra:
        return jsonify({"error": "Obra não encontrada"}), 404
    
    return jsonify(obra.to_dict()), 200

@obras_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar uma obra existente
    ---
    tags:
      - Obras
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Obra'
    responses:
      200:
        description: OK
    """
    obra = Obra.query.get(id)

    if not obra:
        return jsonify({"error": "Obra não encontrada"}), 404
    try:
        data = request.json
        
        obra.endereco = data.get('endereco', obra.endereco)
        obra.data_inicio = data.get('data_inicio', obra.data_inicio)
        obra.previsao_final = data.get('previsao_final', obra.previsao_final)
        obra.cliente = data.get('cliente', obra.cliente)
        obra.valor_contrato = data.get('valor_contrato', obra.valor_contrato)
        obra.nome_profissional = data.get('nome_profissional', obra.nome_profissional)
        
        db.session.commit()
        return jsonify(obra.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@obras_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui uma obra
    ---
    tags:
      - Obras
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
        description: Não encontrada
    """  
    obra = Obra.query.get(id)

    if not obra:
        return jsonify({"error": "Obra não encontrada"}), 404
    
    db.session.delete(obra)
    db.session.commit()

    return jsonify({"mensagem": "Obra removida com sucesso"}), 200