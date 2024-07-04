import shutil

from rdkit import Chem
from rdkit.Chem import inchi


def convert(value: str, from_type: str, to_type:str):
    if from_type == 'SMILES':
        mol = Chem.MolFromSmiles(value)
    elif from_type == 'Inchi':
        mol = inchi.MolFromInchi(value)
    elif from_type == 'SMARTS':
        mol = Chem.MolFromSmarts(value)
    elif from_type == 'MolBlock':
        mol = Chem.MolFromMolBlock(value)


    print(to_type)
    if to_type == 'MolBlock':
        return Chem.MolToMolBlock(mol)
    elif to_type == 'Inchi':
        print("AA")
        return inchi.MolToInchi(mol)
    elif to_type == 'SMARTS':
        return Chem.MolToSmarts(mol)
    elif to_type == 'SMILES':
        return Chem.MolToSmiles(mol)