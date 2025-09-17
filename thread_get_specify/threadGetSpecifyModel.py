from bson import ObjectId
from config.mongodb import get_db

col = get_db()["thread"]

def findPostById(idStr: str):
    if not ObjectId.is_valid(idStr):
        return None
    doc = col.find_one({"_id": ObjectId(idStr)})
    return doc
