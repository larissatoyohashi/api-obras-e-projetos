from pydantic import BaseModel

class ClienteSchema(BaseModel):
    id: int | None = None
    nome: str
    cpf: str
    telefone: int