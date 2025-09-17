from bson import ObjectId
from config.mongodb import get_db

COL = get_db()["posts"]

def find_post_by_id(id_str: str):
    if not ObjectId.is_valid(id_str):
        return None
    doc = COL.find_one({"_id": ObjectId(id_str)})
    return doc

def inc_views(id_str: str):
    if not ObjectId.is_valid(id_str):
        return False
    res = COL.update_one({"_id": ObjectId(id_str)}, {"$inc": {"views": 1}})
    return res.modified_count > 0