from fastapi import APIRouter, UploadFile, File, Query
from router.convertMolecules import manager
router = APIRouter(tags=["RDKit convert"], prefix="/rdkit/convert")


@router.post("/molFileToSmiles/")
async def molFileToSmiles(file: UploadFile = File(...), isomerics: bool = Query(True)):
    return manager.molFileToSmiles(file, isomerics)