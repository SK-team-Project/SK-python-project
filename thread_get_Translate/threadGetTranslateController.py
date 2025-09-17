from flask import Blueprint, request, jsonify
from threadGetTranslateService import translate_post_text

# Blueprint 생성
translate = Blueprint('translate', __name__, url_prefix='/translate')

@translate.route("/", methods=["POST"])
def translate():
    # JSON 형식이라면
    data = request.get_json()
    text = data.get("text", "")
    
    # Service로 전달
    translated = translate_post_text(text)
    
    return jsonify({"translated": translated})