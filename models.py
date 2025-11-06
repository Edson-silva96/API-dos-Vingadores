
from pydantic import BaseModel
from typing import List, Union

class Heroi(BaseModel):
    Nome: str
    Identidade_Secreta: str
    Poder: str
    Habilidade: Union[List[str], str]
    Arma: str
