from pydantic import BaseModel

class ObraSchema(BaseModel):
    id: int | None = None
    endereco: str
    data_inicio: str
    previsao_final: str
    cliente: str
    valor_contrato: float
    nome_profissional : str