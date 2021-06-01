from pydantic import BaseModel
from typing import Optional, List

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    #legendas: List[legendas] = []

   


class Legenda(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    pais: str
    disponivel: bool = False
    genero: str
    ano: int

    class Config():
        orm_mode = True






