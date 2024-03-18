from typing import Optional
from pydantic import BaseModel

class MaravilhasDoMundo (BaseModel):
    id: Optional[int] = None
    nome: str 
    localizacao: str 
    descricao: str 
    