from flask import Blueprint, render_template, abort, request
from .threadGetSpecifyService import get_post_detail

thread_spec_bp = Blueprint("thread_spec", __name__, url_prefix="/thread")

@thread_spec_bp.get("/<post_id>")
def get_one(post_id):
    inc = request.args.get("incViews", "true").lower() != "false"
    result = get_post_detail(post_id, with_inc_views=inc)
    if not result["ok"]:
        abort(result["status"])
    return render_template("thread_detail.html", post=result["data"])
