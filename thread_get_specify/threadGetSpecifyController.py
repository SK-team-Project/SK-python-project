from flask import Blueprint, render_template, abort, request
from .threadGetSpecifyService import getPostDetail

threadSpecBp = Blueprint("threadSpec", __name__, url_prefix="/thread")

@threadSpecBp.get("/<postId>")
def getOne(postId):
    result = getPostDetail(postId)
    if not result["ok"]:
        abort(result["status"])
    return render_template("thread_spe.html", post=result["data"])