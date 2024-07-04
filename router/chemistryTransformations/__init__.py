from fastapi import APIRouter
from router.chemistryTransformations import manager

router = APIRouter(tags=["RDKit chemistry transformations"], prefix="/rdkit/transformations")


@router.get("/removeSubstructure")
def remove_substructure(baseType: str, mol: str, subType: str, sub: str):
    return manager.remove_substructure(baseType, mol, subType, sub)


@router.get("/replaceSubstructure")
def replace_substructure(baseType: str, mol: str, pattType: str, patt: str,replType:str, repl:str):
    return manager.replace_substructure(baseType, mol, pattType, patt, replType, repl)

@router.get("/removeLateralChains")
def remove_lateral_chains(baseType: str, mol: str, coreType: str, core: str):
    return manager.remove_lateral_chains(baseType, mol, coreType, core)


@router.get("/removeCore")
def remove_core(baseType: str, mol: str, coreType: str, core: str):
    return manager.remove_core(baseType, mol, coreType, core)




