from .threadGetSpecifyModel import find_post_by_id, inc_views

def get_post_detail(post_id: str, with_inc_views: bool = True):
    doc = find_post_by_id(post_id)
    if not doc:
        return {"ok": False, "status": 404, "error": "NOT_FOUND"}

    if with_inc_views:
        inc_views(post_id)
        try:
            doc["views"] = int(doc.get("views") or 0) + 1
        except Exception:
            pass

    doc["id"] = str(doc.pop("_id"))
    return {"ok": True, "status": 200, "data": doc}