import pymongo

from .session import MongoClient

def index_mongo_collections():

    # craft_multi_token
    MongoClient["icon"]["craft_multi_token_contract"].create_index([("block_number", -1)])
    MongoClient["icon"]["craft_multi_token_contract"].create_index([("method", "hashed")])
    MongoClient["icon"]["craft_multi_token_contract"].create_index([("type", "hashed")])
