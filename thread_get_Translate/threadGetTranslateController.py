from flask import Blueprint, request, jsonify
from thread_get_Translate.threadGetTranslateService import translate_post_text

# Blueprint 생성
translate = Blueprint('translate', __name__, url_prefix='/translate')

@translate.route("/", methods=["POST"])
#이름 중복으로 오류떠서 do_추가했습니다
def do_translate():
    # JSON 형식이라면
    data = request.get_json()
    text = data.get("text", "")
    
    # Service로 전달
    translated = translate_post_text(text)
    
    return jsonify({"translated": translated})