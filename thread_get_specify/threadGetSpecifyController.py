from flask import Blueprint, render_template, abort, request
from .threadGetSpecifyService import getPostDetail

threadSpecBp = Blueprint("threadSpec", __name__, url_prefix="/thread")

@threadSpecBp.get("/<thread_id>")
def getOne(thread_id):
    result = getPostDetail(thread_id)
    if not result["ok"]:
        abort(result["status"])
    return render_template("thread_spe.html", post=result["data"])