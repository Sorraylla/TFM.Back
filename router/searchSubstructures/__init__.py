from fastapi import APIRouter
from router.searchSubstructures import manager

router = APIRouter(tags=["RDKit substructures"], prefix="/rdkit/substructures")


@router.get("/molecules/")
def substructure(typeMol: str, mol:str, typeSub: str, sub: str):
    return manager.substructure(typeMol, mol, typeSub, sub)


"""
@router.get("/myMolecules/")
def substructure_fom_my_molecules(name: str, type: str, substr: str):
    return manager.substructure_fom_my_molecules(name,type, substr)

"""
