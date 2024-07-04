from io import BytesIO

from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from starlette.responses import StreamingResponse


def remove_substructure(baseType: str, mol: str, subType: str, sub: str):
    if baseType == 'SMILES':
        m = Chem.MolFromSmiles(mol)
    elif baseType == 'SMARTS':
        m = Chem.MolFromSmarts(mol)

    if subType == 'SMILES':
        patt = Chem.molFromSmiles(sub)
    if subType == 'SMARTS':
        patt = Chem.MolFromSmarts(sub)
    rm = AllChem.DeleteSubstructs(m, patt)
    smiles = Chem.MolToSmiles(rm)

    m = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(m)

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")



def replace_substructure(baseType: str, mol: str, pattType: str, patt: str,replType:str, repl:str):
    if baseType == 'SMILES':
        m = Chem.MolFromSmiles(mol)
    elif baseType == 'SMARTS':
        m = Chem.MolFromSmarts(mol)

    if pattType == 'SMILES':
        patt = Chem.MolFromSmiles(patt)

    if pattType == 'SMARTS':
        patt = Chem.MolFromSmarts(patt)

    if replType == 'SMILES':
        repl = Chem.MolFromSmiles(repl)

    if replType == 'SMARTS':
        repl = Chem.MolFromSmarts(repl)

    # Realizar el reemplazo
    rms = AllChem.ReplaceSubstructs(m, patt, repl)

    # Convertir la molécula resultante a SMILES
    smiles = Chem.MolToSmiles(rms[0])
    m = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(m)

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")




def remove_lateral_chains(baseType: str, mol: str, coreType: str, core: str):
    if baseType == 'SMILES':
        m = Chem.MolFromSmiles(mol)
    elif baseType == 'SMARTS':
        m = Chem.MolFromSmarts(mol)

    if coreType == 'SMILES':
        core = Chem.MolFromSmiles(core)
    if coreType == 'SMARTS':
        core = Chem.MolFromSmarts(core)

    # Reemplazar las cadenas laterales
    tmp = Chem.ReplaceSidechains(m, core)

    # Convertir a SMILES
    smiles = Chem.MolToSmiles(tmp)
    m = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(m)

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")


def remove_core(baseType: str, mol: str, coreType: str, core: str):
    if baseType == 'SMILES':
        m = Chem.MolFromSmiles(mol)
    elif baseType == 'SMARTS':
        m = Chem.MolFromSmarts(mol)

    if coreType == 'SMILES':
        core = Chem.MolFromSmiles(core)
    if coreType == 'SMARTS':
        core = Chem.MolFromSmarts(core)

    # Reemplazar las cadenas laterales
    tmp = Chem.ReplaceCore(m,core)

    # Convertir a SMILES
    smiles = Chem.MolToSmiles(tmp)
    m = Chem.MolFromSmiles(smiles)
    img = Draw.MolToImage(m)

    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    return StreamingResponse(BytesIO(img_byte_arr), media_type="image/png")