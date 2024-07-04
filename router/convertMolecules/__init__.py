from fastapi import APIRouter, UploadFile, File, Query

from model.convertInfo import ConversionRequest
from router.convertMolecules import manager
router = APIRouter(tags=["RDKit convert"], prefix="/rdkit/convert")


@router.post("/")
def convert(request: ConversionRequest):
    return manager.convert(request.value, request.from_type, request.to_type)