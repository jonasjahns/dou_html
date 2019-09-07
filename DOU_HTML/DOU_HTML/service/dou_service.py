from dataclasses import asdict

from pymongo import MongoClient


def client_start():
    client = MongoClient('mongodb://127.0.0.1:27017')
    return client


def database_start(db_name: str):
    client = client_start()
    return client[db_name]


def collection_start(col_name: str):
    client = database_start("licitacoes")
    return client[col_name]


def salva_obj(objeto, client):
    db = collection_start(client)
    obj_dict = asdict(objeto)
    print(db.insert_one(obj_dict).inserted_id)


def find_all(client):
    db = collection_start(client)
    return db.find()


def delete(client, query):
    db = collection_start(client)
    print(db.delete_one(query))


def find_one(client):
    db = collection_start(client)
    return db.find_one()
