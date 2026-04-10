from pydantic import BaseModel

class ProjetoSchema(BaseModel):
    id: int | None = None
    categoria: str
    data_contrato: str
    cliente: str
    valor_contrato: float
    art : float
    nome_profissional : str