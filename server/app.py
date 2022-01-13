# 플라스크 자체를 로딩

from flask import Flask, request

from server.db_connector import DBConnector

# DB연결 정보를 관리하는 클래스 생성해서, 객체를 변수에 담아두자
db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    # API로직 함수,클래스들은 create_app 함수 내에서만 필요함
    # 함수 내부에서 import를 실행하도록 구조를 변경함 => 순환참조를 피해서 정상동작할 수 있게 유도함
    from .api.user import login, sign_up, find_user_by_email
    from .api.lecture import get_all_lecture
    
    # 기본 로그인 기능 주소 열어주기
    @app.post("/user")
    def user_post():
        # args(GET/DELETE) 변수에는 쿼리 파라미터에 들어있는 데이터들이 담겨있다
        # 폼데이터에 담겨있는 데이터를 꺼내려면 form(PUT/PATCH/POST)에 담아줘야 함
        # cf) json body 첨부하는 경우도 있다(최신스텍)
        return login(request.form.to_dict())

    
    # 회원가입 기능 주소 열어주기
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    
    # 유저 이메일 조회 기능 주소 열어주기
    @app.get("/user")
    def user_get():
        return find_user_by_email(request.args.to_dict())
    
    
    @app.post("/lecture")
    def lecture_post():
        return lecture_test()
    
    
    return app