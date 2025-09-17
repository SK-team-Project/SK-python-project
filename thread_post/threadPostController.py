from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from config.mongodb import get_db
from user.userService import loginService, generateCode

thread = Blueprint('user', __name__, url_prefix='/user')

@thread.route('/thread/write', methods=['GET'])


def writePage():
    return render_template('thread_write.html')

# 글 작성 처리 (POST)
@thread.route('/thread/write', methods=['POST'])

def writePost():
    db = get_db("sk27")          
    threads = db['thread']       

    title = request.form['title']
    body = request.form['body']

    threads.insert_one({
        "threadTitle": title,
        "threadBody": body,
        "uploadDate": datetime.utcnow()
    })

    return redirect(url_for('user.allThreads'))


# 글 전체 보기 (목록)
@thread.route('/thread/all', methods=['GET'])
def allThreads():
    db = get_db("sk27")
    threads = db['thread'].find().sort("uploadDate", -1)
    return render_template('thread_all.html', threads=threads)