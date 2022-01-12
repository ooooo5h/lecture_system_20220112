# 로그인 / 회원가입 등 실제 사용자 정보 관련된 기능들을 모아두는 모듈
# DB연결정보를 보관한 변수를 import하면 쉽게 쓰겠지?
from server.db_connector import DBConnector
from server.model import Users

db = DBConnector()

def test():
    
    # DB의 모든 users를 조회하는 쿼리를 테스트로 날려보자
    sql = f"SELECT * FROM users"
    all_list = db.executeAll(sql)
    
    # 목록을 for문을 돌면서, 한 줄을 row로 추출하고, 추출된 row로 모델클래스로 가공해서 dict로 재가공을 한 줄로 마무리할 수 있음
    # python for문을 list 내부를 돌면서 채워준다 => comprehension
    all_users = [ Users(row).get_data_object()  for row in all_list]   
    
        
    return {
        'users' : all_users,
    }