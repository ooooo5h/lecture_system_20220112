# 플라스크 자체를 로딩

from flask import Flask, request

from server.db_connector import DBConnector

# DB연결 정보를 관리하는 클래스 생성해서, 객체를 변수에 담아두자
db = DBConnector()

def create_app():
    app = Flask(__name__)
      
    # API 로직 함수/클래스들은 create_app() 함수 내부에서만 필요
    from .api.user import login, sign_up, find_user_by_email
    from .api.lecture import get_all_lectures, apply_lecture, cancel_apply, write_review
    
    # 기본 로그인 기능 주소 열어주기
    @app.post("/user")
    def user_post():
        # args 변수에는 쿼리 파라미터에 들어있는 데이터들이 담겨있다
        # 폼데이터에 담겨있는 데이터를 꺼내려면 form에 담아줘야 함
        return login(request.form.to_dict())
    
    
    # 회원가입 기능 주소 열어주기
    @app.put("/user")
    def user_put():
        return sign_up(request.form.to_dict())
    
    
    # 유저 이메일 확인 기능 주소 열어주기
    @app.get("/user")
    def user_get():
        return find_user_by_email(request.args.to_dict())
    
    
    ## 모든 강의 목록 조회
    @app.get("/lecture")
    def lecture_get():
        return get_all_lectures(request.args.to_dict())
    
    
    ## 수강신청
    @app.post("/lecture")
    def lecture_post():
        return apply_lecture(request.form.to_dict())
    
    
    ## 수강취소
    @app.delete("/lecture")
    def lecture_delete():
        return cancel_apply(request.args.to_dict())
    
    
    ### 강의 리뷰 작성
    @app.post("/lecture/review")
    def review_post():
        return write_review(request.form.to_dict())
    
    return app