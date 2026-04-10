from flask import Blueprint, request, jsonify
from ..database import db
from ..models import Projeto
from ..schemas.projeto_schema import ProjetoSchema
from pydantic import ValidationError

projetos_bp = Blueprint('projetos', __name__, url_prefix='/projetos')


@projetos_bp.route('/', methods=['POST'])
def create():
    """
    Criar um novo Projeto
    ---
    tags:
      - Projetos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/Projeto'
    responses:
      201:
        description: Projeto criado com sucesso
        schema:
          $ref: '#/definitions/Projeto'
    """
    try:
       data = ProjetoSchema(**request.json)
       novo_projeto = Projeto(**data.model_dump(exclude_none=True))
       db.session.add(novo_projeto)
       db.session.commit()
       
       return jsonify(novo_projeto.to_dict()), 201
    except ValidationError as err:
      return jsonify({"errors": err.errors()}), 400

@projetos_bp.route('/', methods=['GET'])
def get_all():
    """
    Lista todos os projetos
    ---
    tags:
      - Projetos
    responses:
      200:
        description: OK
    """
    projetos = Projeto.query.all()
    result = [ProjetoSchema(**p.to_dict()).model_dump() for p in projetos]
    return jsonify(result), 200

@projetos_bp.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    """
    Lista um projeto específico pelo ID
    ---
    tags:
      - Projetos
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
    projeto = Projeto.query.get(id)

    if not projeto:
        return jsonify({"error": "Projeto não encontrado"}), 404
    
    return jsonify(projeto.to_dict()), 200

@projetos_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    """
    Atualizar um projeto existente
    ---
    tags:
      - Projetos
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Projeto'
    responses:
      200:
        description: OK
    """
    projeto = Projeto.query.get(id)

    if not projeto:
        return jsonify({"error": "Projeto não encontrado"}), 404
    try:
        data = request.json
        
        projeto.categoria = data.get('categoria', projeto.categoria)
        projeto.data_contrato = data.get('data_contrato', projeto.data_contrato)
        projeto.cliente = data.get('cliente', projeto.cliente)
        projeto.valor_contrato = data.get('valor_contrato', projeto.valor_contrato)
        projeto.art = data.get('art', projeto.art)
        projeto.nome_profissional = data.get('nome_profissional', projeto.nome_profissional)
        
        db.session.commit()
        return jsonify(projeto.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@projetos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Exclui um projeto
    ---
    tags:
      - Projetos
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
    projeto = Projeto.query.get(id)

    if not projeto:
        return jsonify({"error": "Projeto não encontrado"}), 404
    
    db.session.delete(projeto)
    db.session.commit()

    return jsonify({"mensagem": "Projeto removido com sucesso"}), 200