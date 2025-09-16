# SK 쉴더스 Python project
Sk 쉴더스 Python Project 입니다.

## Git Rows
1. git issue 템플릿은 "SK 이슈 템플릿"을 사용할 것
2. issue 제목은 [feat], [refac], [document], [fix], [hotfix] + 제목으로 할 것
3. issue 내용은 작업 내용을 적을 것
4. issue 를 파고 branch 생성 이후 본인 작업 진행
5. branch 작업이 끝난 이후 PR 올리기
6. PR에 reviewer는 gjuni와 friedpenguin80 를 반드시 참조 후 comment 이후 Merge 할 것

## Code Convention
1. 함수와 변수명은 반드시 Carmel Case를 사용할 것

## File 구조
DDD : Domain Driven Design
: 각 기능 별로 파일을 나눔.

<pre>
<code>
  SK-python-project/
├── README.md
├── requirements.txt
├── .gitignore
├── app.py                   
├── 
├── templates/                # HTML 템플릿 파일들
│   ├── index.html           # 메인 페이지 
│   ├── thread_all.html      # 스레드 목록 페이지 
│   └── user.html            # 사용자 페이지 
├── 
├── static/                   # 정적 파일들
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── 
├── config/                  
│   ├── __init__.py
│   └── mongodb.py
│   
├── 
├── user/                   
│   ├── __init__.py
│   ├── userController.py
│   ├── userService.py
│   └── userModel.py
</code>  
</pre>

