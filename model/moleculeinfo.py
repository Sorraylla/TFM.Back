from enum import Enum
from typing import Optional

from pydantic import BaseModel


class NewMoleculeInfo(BaseModel):
    name: Optional[str]
    userId: int
    image: str
    smiles: Optional[str] = None
    date: int

class MoleculeInfo(NewMoleculeInfo):
    id: str


class Supplier(Enum):
    modelo_a = "Modelo A"
    modelo_b = "Modelo B"
    modelo_c = "Modelo C"

