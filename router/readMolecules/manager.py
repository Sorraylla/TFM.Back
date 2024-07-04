import shutil

from fastapi.responses import StreamingResponse
from rdkit import Chem
from rdkit.Chem import Draw
from io import BytesIO

from model.moleculeinfo import MoleculeInfo, NewMoleculeInfo
from db.mongo import molecules as molecules_dao


def generate_from_smiles(smiles: str):
    m = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(m)

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")


def generate_from_file(file):
    with open("temp.mol", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    m = Chem.MolFromMolFile("temp.mol")
    img = Draw.MolToImage(m)

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")


def read_group_files(file):
    with open("temp.sdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    natoms = []
    suppl = Chem.SDMolSupplier('temp.sdf')
    for mol in suppl:
        natoms.append(mol.GetNumAtoms())

    return natoms

def insert_molecule(molecule: NewMoleculeInfo):
    result_id = molecules_dao.insert_molecule(molecule)
    print(result_id)
    result = molecules_dao.get_molecule_by_id(result_id)
    if result:
        result["id"] = str(result["_id"])
        return MoleculeInfo.parse_obj(result)


def remove_molecule(id_molecule: str):
    result = molecules_dao.remove_molecule(id_molecule)
    if result:
        return "OK"

def update_molecule(mol: MoleculeInfo):
    result = molecules_dao.update_molecule(mol)
    if result:
        result['id'] = str(result['_id'])
        return MoleculeInfo.parse_obj(result)



def get_molecule_by_user(userId: int):
    result = molecules_dao.get_molecule_by_user(userId)
    molecules = []
    if result:
        for mol in result:
            mol['id']= str(mol['_id'])
            molecules.append(MoleculeInfo.parse_obj(mol))
    return molecules