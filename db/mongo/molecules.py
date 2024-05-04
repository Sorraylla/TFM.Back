from bson import ObjectId

from model.moleculeinfo import MoleculeInfo, NewMoleculeInfo
from db.mongo.connector import connection


def insert_molecule(molecule: NewMoleculeInfo):
    return connection.molecules.insert_one(molecule.dict()).inserted_id


def get_molecule_by_user(userId: int):
    return connection.molecules.find({"userId": userId})


def get_molecule_by_id(id: str):
    return connection.molecules.find_one({"_id": ObjectId(id)})
