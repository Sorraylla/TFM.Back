import shutil

from rdkit import Chem


def molFileToSmiles(file, isomerics):
    with open("temp.mol", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    m = Chem.MolFromMolFile("temp.mol")
    return Chem.MolToSmiles(m, isomericSmiles = isomerics)


def smilesToMol():
    return None



def molToMolBlock():
    return None