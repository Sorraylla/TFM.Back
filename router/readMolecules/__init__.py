from fastapi import APIRouter, UploadFile, File

from model.moleculeinfo import MoleculeInfo, NewMoleculeInfo
from router.readMolecules import manager

router = APIRouter(tags=["RDKit read"], prefix="/rdkit")

## Librería
@router.get("/read/simple/smiles/")
def generate_from_smiles(smiles: str):
    return manager.generate_from_smiles(smiles)


@router.post("/read/simple/files/")
async def generate_from_files(file: UploadFile = File(...)):
    return manager.generate_from_file(file)

@router.post("/read/group/files/")
async def read_group_files(file: UploadFile = File(...)):
    return manager.read_group_files(file)

##DB
@router.post("/molecule/")
def insert_molecule(molecule: NewMoleculeInfo):
    return manager.insert_molecule(molecule)


@router.get("/molecules/")
def get_molecule_by_user(userId: int):
    return manager.get_molecule_by_user(userId)