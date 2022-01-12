# 플라스크 자체를 로딩

from flask import Flask

from server.db_connector import DBConnector

from .api.user import test

# DB연결 정보를 관리하는 클래스 생성해서, 객체를 변수에 담아두자
db = DBConnector()

def create_app():
    app = Flask(__name__)
    
    @app.get("/test")
    def api_test():
        return test()
    
    return app