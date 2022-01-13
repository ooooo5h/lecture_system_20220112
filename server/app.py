# 플라스크 자체를 로딩

from flask import Flask, request

from server.db_connector import DBConnector

# DB연결 정보를 관리하는 클래스 생성해서, 객체를 변수에 담아두자
db = DBConnector()

def create_app():
    app = Flask(__name__)
      
    # API 로직 함수/클래스들은 create_app() 함수 내부에서만 필요
    from .api.user import login, sign_up, find_user_by_email
    from .api.lecture import get_all_lectures
    
    # 기본 로그인 기능 주소 열어주기
    @app.post("/user")
    def user_post():
        # args 변수에는 쿼리 파라미터에 들어있는 데이터들이 담겨있다
        # 폼데이터에 담겨있는 데이터를 꺼내려면 form에 담아줘야 함
        return login(request.form.to_dict())


    @app.post("/lecture")
    def lecture_post():
        return get_all_lectures()
    
    
    # 회원가입 기능 주소 열어주기
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    
    # 유저 이메일 확인 기능 주소 열어주기
    @app.get("/user")
    def user_get():
        return find_user_by_email(request.args.to_dict())
    
    return app