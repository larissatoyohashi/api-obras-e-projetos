from pydantic import BaseModel

class ProfissionalSchema(BaseModel):
    id: int | None = None
    categoria: str
    nome: str
    num_crea: str
    salario: float