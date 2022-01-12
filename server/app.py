# 플라스크 자체를 로딩

from flask import Flask, request

from server.db_connector import DBConnector

from .api.user import login
from .api.lecture import lecture_test

# DB연결 정보를 관리하는 클래스 생성해서, 객체를 변수에 담아두자
# db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    # 기본 로그인 기능 주소 열어주기
    @app.post("/user")
    def user_post():
        return login(request.args.to_dict())


    @app.post("/lecture")
    def lecture_post():
        return lecture_test()
    
    return app