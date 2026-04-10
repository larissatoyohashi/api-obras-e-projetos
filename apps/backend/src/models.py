from .database import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String, nullable=False, unique=True)
    telefone = db.Column(db.String) # Usando String para evitar erros com números grandes

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Profissional(db.Model):
    __tablename__ = 'profissionais'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String, nullable=False)
    nome = db.Column(db.String, nullable=False)
    num_crea = db.Column(db.String, nullable=False, unique=True)
    salario = db.Column(db.Float)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Obra(db.Model):
    __tablename__ = 'obras'
    id = db.Column(db.Integer, primary_key=True)
    endereco = db.Column(db.String, nullable=False)
    data_inicio = db.Column(db.String)
    previsao_final = db.Column(db.String)
    cliente = db.Column(db.String, nullable=False) 
    valor_contrato = db.Column(db.Float)
    nome_profissional = db.Column(db.String) 

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Projeto(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String, nullable=False)
    data_contrato = db.Column(db.String)
    cliente = db.Column(db.String, nullable=False) 
    valor_contrato = db.Column(db.Float)
    art = db.Column(db.Float)
    nome_profissional = db.Column(db.String) 

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}