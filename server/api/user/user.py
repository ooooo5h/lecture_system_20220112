# 로그인 / 회원가입 등 실제 사용자 정보 관련된 기능들을 모아두는 모듈
# DB연결정보를 보관한 변수를 import하면 쉽게 쓰겠지?
from server.db_connector import DBConnector
from server.model import Users

db = DBConnector()


# 로그인 기능
def login(params):
    sql = f"SELECT * FROM users WHERE email ='{params['email']}' AND password = '{params['pw']}'"
    
    login_user = db.executeOne(sql)   # 있다면 인스턴스가 있고, 없다면 None으로 나올 것
    
    if login_user is None :
        return {
            'code' : 400,
            'message' : '이메일 or 비밀번호 오류',
        }, 400
        
    return {
        'code' : 200,
        'message' : '로그인 성공',
        'data' : {
            'user' : Users(login_user).get_data_object()
        }
    }
    
# 회원가입 기능
def sign_up(params):
    
    ## 도전과제 1 : 회원가입시 중복된 이메일이면 400 처리
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    email_check_result = db.executeOne(sql)
    
    if email_check_result :
        return {
            'code' : 400,
            'message' : '중복된 이메일입니다.'
        }, 400  
    
    sql = f"INSERT INTO users (email, password, name) VALUES ('{params['email']}', '{params['pw']}', '{params['name']}')"
    
    db.insetAndCommit(sql)
    
    return {
        'code' : 200,
        'message' : '회원가입 성공2',
    }
    
    
# 이메일 조회 기능
def check_user_email(params):
    
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    user_email_check_result = db.executeOne(sql)
    
    if user_email_check_result is None:
        return {
            'code' : 400,
            'message' : '해당 이메일의 사용자는 존재하지 않습니다.',
        }, 400
        
    return {
        'code' : 200,
        'message' : '해당 이메일 있음',
        'data' : {
            'user' : Users(user_email_check_result).get_data_object()
        }
    }