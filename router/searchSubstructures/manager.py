from rdkit import Chem
from db.mongo import molecules as molecules_dao
from model.moleculeinfo import MoleculeInfo


def substructure(typeMol:str, mol:str, typeSub:str, sub:str):
    if typeMol == 'SMILES':
        m = Chem.MolFromSmiles(mol)
    elif typeMol == 'SMARTS':
        m = Chem.MolFromSmarts(mol)

    if typeSub == 'SMILES':
        patt = Chem.MolFromSmiles(sub)
    elif typeSub == 'SMARTS':
        patt = Chem.MolFromSmarts(sub)

    index = m.GetSubstructMatches(patt)
    if index:
        return index




def substructure_fom_my_molecules(name:str,type:str, substr:str):
    mol = molecules_dao.get_molecule_by_name(name)
    if mol:
        mol['id']= str(mol['_id'])
        mol = MoleculeInfo.parse_obj(mol)
        m = Chem.MolFromSmiles(mol.smiles)
        if type == 'SMILES':
            patt = Chem.MolFromSmiles(substr)
        elif type == 'SMARTS':
            patt = Chem.MolFromSmarts(substr)
        index = m.GetSubstructMatches(patt)
        if index:
            return index
