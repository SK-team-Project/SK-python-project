from .threadGetSpecifyModel import findPostById

def getPostDetail(postId: str):
    doc = findPostById(postId)
    if not doc:
        return {"ok": False, "status": 404, "error": "NOT_FOUND"}

    doc["id"] = str(doc.pop("_id"))
    return {"ok": True, "status": 200, "data": doc}