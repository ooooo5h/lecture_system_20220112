# 로그인 / 회원가입 등 실제 사용자 정보 관련된 기능들을 모아두는 모듈
# DB연결정보를 보관한 변수를 import하면 쉽게 쓰겠지?
from server.db_connector import DBConnector
from server.model import Users

db = DBConnector()

def test():
    
    # DB의 모든 users를 조회하는 쿼리를 테스트로 날려보자
    sql = f"SELECT * FROM users"
    db.cursor.execute(sql)
    all_list = db.cursor.fetchall()
    
    all_users = [] 
    
    for row in all_list:
        
        # Users(row) : Users형태의 인스턴스 생성 => 함수들도 내장하고 있다
        # 인스턴스에게 곧바로 get_data_object()를 실행하는 명령을 내림
        # 해당 유저의 정보를 활용한 dict가 리턴되..........
        # 곧바로 목록의 append의 재료로 활용
        all_users.append(Users(row).get_data_object())
        
    return {
        'users' : all_users,
    }