from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Profissional
from ..schemas.profissional_schema import ProfissionalSchema
from pydantic import ValidationError

profissionais_bp = Blueprint('profissionais', __name__, url_prefix='/profissionais')

@profissionais_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo Profissional
    ---
    tags:
      - Profissionais
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Profissional'
    responses:
      201:
        description: Profissional criado com sucesso
        schema:
          $ref: '#/definitions/Profissional'
    """
    try:
       data = ProfissionalSchema(**request.json)
       novo_profissional = Profissional(**data.model_dump(exclude_none=True))
       db.session.add(novo_profissional)
       db.session.commit()
       
       return jsonify(novo_profissional.to_dict()), 201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400

@profissionais_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os profissionais
    ---
    tags:
      - Profissionais
    responses:
      200:
        description: OK
    """
    profissionais = Profissional.query.all()
    result = [ProfissionalSchema(**p.to_dict()).model_dump() for p in profissionais]
    return jsonify(result), 200

@profissionais_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um profissional específico pelo ID
    ---
    tags:
      - Profissionais
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
    profissional = Profissional.query.get(id)

    if not profissional:
        return jsonify({"error": "Profissional não encontrado"}), 404
    
    return jsonify(profissional.to_dict()), 200


@profissionais_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um profissional existente
    ---
    tags:
      - Profissionais
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Profissional'
    responses:
      200:
        description: OK
    """
    profissional = Profissional.query.get(id)

    if not profissional:
        return jsonify({"error": "Profissional não encontrado"}), 404
    try:
        data = request.json
        
        profissional.categoria = data.get('categoria', profissional.categoria)
        profissional.nome = data.get('nome', profissional.nome)
        profissional.num_crea = data.get('num_crea', profissional.num_crea)
        profissional.salario = data.get('salario', profissional.salario)
        
        db.session.commit()
        return jsonify(profissional.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@profissionais_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um profissional
    ---
    tags:
      - Profissionais
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
    profissional = Profissional.query.get(id)

    if not profissional:
        return jsonify({"error": "Profissional não encontrado"}), 404
    
    db.session.delete(profissional)
    db.session.commit()

    return jsonify({"mensagem": "Profissional removido com sucesso"}), 200