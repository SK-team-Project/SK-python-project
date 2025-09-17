from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from config.mongodb import get_db
from bson.objectid import ObjectId   # detail 조회 시 필요

thread = Blueprint('threadAll', __name__, url_prefix='/threadAll')

@thread.route('/write', methods=['GET'])
def writePage():
    print("check writepage")
    return render_template('thread_write.html')

# 글 작성 처리 (POST)
@thread.route('/upload', methods=['POST'])
def writePost():
    print("check writepost")
    db = get_db("sk27")          
    threads = db['thread']       

    title = request.form['title']
    body = request.form['body']

    threads.insert_one({
        "threadTitle": title,
        "threadBody": body,
        "uploadDate": datetime.utcnow()
    })

    return redirect(url_for('threadAll.allThreads')) 

# 글 전체 보기 (목록)
@thread.route('/all', methods=['GET'])
def allThreads():
    print("check allthread")
    db = get_db("sk27")
    threads = db['thread'].find().sort("uploadDate", -1)
    return render_template('thread_all.html', threads=threads)

# 글 상세 정보 보기
@thread.route('/detail/<thread_id>', methods=['GET'])
def detail(thread_id):
    db = get_db("sk27")
    thread_data = db['thread'].find_one({"_id": ObjectId(thread_id)})
    return render_template('thread_detail.html', thread=thread_data)