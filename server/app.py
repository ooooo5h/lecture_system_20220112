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
    from .api.lecture import get_all_lecture, apply_lecture, cancel_apply, write_review, view_lecture_detail
    
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
    
    
    ## 모든 강의 목록 조회
    @app.get("/lecture")
    def lecture_get():
        return get_all_lecture(request.args.to_dict())
    
    
    ## 특정 강의 상세 조회
    @app.get("/lecture/<lecture_id>")    # /lecture/1   처럼, path방식의 주소를 작성하고 싶다
    def lecture_detail(lecture_id):
        print(f"어떤 강의 보고싶니 {lecture_id}")
        return view_lecture_detail()
    
        
    ## 수강 신청
    @app.post("/lecture")
    def lecture_post():
        return apply_lecture(request.form.to_dict())
    
    
    ## 수강 취소
    @app.delete("/lecture")
    def lecture_delete():
        return cancel_apply(request.args.to_dict())
    
    
    ## 강의 리뷰 작성
    @app.post("/lecture/review")
    def review_post():
        return write_review(request.form.to_dict())
    
    return app