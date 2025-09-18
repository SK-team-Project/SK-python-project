from flask import Flask
# 1. user.Controller 파일에서 생성한 user_bp 블루프린트 객체를 가져옵니다.
from user.userController import user
from thread_post.threadPostController import thread
from thread_get_specify.threadGetSpecifyController import threadSpecBp
from thread_get_Translate.threadGetTranslateController import translate
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/back')
def back():
    return render_template('thread_all.html')

app.register_blueprint(user) 
app.register_blueprint(thread)
app.register_blueprint(threadSpecBp)
app.register_blueprint(translate)

if __name__ == "__main__":
    app.run(debug=True)