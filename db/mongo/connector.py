import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/rdkit")
connection = client["rdkit"]

