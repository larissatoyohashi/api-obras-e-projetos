from flask import Flask
from flasgger import Swagger
import os
from dotenv import load_dotenv
from .database import init_db, db

# SCHEMAS
from .schemas.cliente_schema import ClienteSchema
from .schemas.obra_schema import ObraSchema
from .schemas.profissional_schema import ProfissionalSchema
from .schemas.projeto_schema import ProjetoSchema

load_dotenv()

def create_app():
    app = Flask(__name__)
    init_db(app)

    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "API Obras e Projetos",
            "description": "API para gestão de Obras e Projetos de um escritório de engenharia",
            "version": "1.0.0"
        },
        "definitions": {
            "Cliente": ClienteSchema.model_json_schema(),
            "Obra": ObraSchema.model_json_schema(),
            "Profissional": ProfissionalSchema.model_json_schema(),
            "Projeto": ProjetoSchema.model_json_schema(),
            "Error": {
                "type": "object",
                "properties": {"error": {"type": "string"}}
            }
        }
    }

    Swagger(app, template=swagger_template)

    from .routes.clientes import clientes_bp
    from .routes.obras import obras_bp
    from .routes.profissionais import profissionais_bp
    from .routes.projetos import projetos_bp

    app.register_blueprint(clientes_bp)
    app.register_blueprint(obras_bp)
    app.register_blueprint(profissionais_bp)
    app.register_blueprint(projetos_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)