from thread_get_Translate.threadGetTranslateModel import translate_text

def translate_post_text(text):
    try:
        translated = translate_text(text)
        return translated
    except Exception as e:
        # 로그 기록
        #print(f"[Translate Error] {e}")
        return ""