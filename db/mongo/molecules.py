from bson import ObjectId
from pymongo import ReturnDocument

from model.moleculeinfo import MoleculeInfo, NewMoleculeInfo
from db.mongo.connector import connection


def insert_molecule(molecule: NewMoleculeInfo):
    return connection.molecules.insert_one(molecule.dict()).inserted_id

def remove_molecule(id_molecule:str):
    return connection.molecules.delete_one({'_id': ObjectId(id_molecule)})


def update_molecule(molecule: MoleculeInfo):
    return connection.molecules.find_one_and_update({'_id': ObjectId(molecule.id)}, {"$set": {
        "name": molecule.name,
        "date": molecule.date
    },
    },return_document = ReturnDocument.AFTER)
def get_molecule_by_user(userId: int):
    return connection.molecules.find({"userId": userId})

def get_molecule_by_name(name:str):
    return connection.molecules.find_one({"name": name})


def get_molecule_by_id(id: str):
    return connection.molecules.find_one({"_id": ObjectId(id)})
