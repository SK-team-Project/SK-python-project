from deep_translator import GoogleTranslator

def translate_text(text, source="ko", target="en"):
    #본문내용이 없다면 빈 내용으로 반환
    if not text:
        return ""
    return GoogleTranslator(source=source, target=target).translate(text)