# 로그인 / 회원가입 등 실제 사용자 정보 관련된 기능들을 모아두는 모듈
# DB연결정보를 보관한 변수를 import하면 쉽게 쓰겠지?
from server.model import Users
from server import db

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
    
    db.insertAndCommit(sql)
    
    return {
        'code' : 200,
        'message' : '회원가입 성공',
    }
    
    
# 이메일 조회 기능
def find_user_by_email(params):
    
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    find_user_email_result = db.executeOne(sql)
    
    if find_user_email_result :
        
        found_user = Users(find_user_email_result)   
        return {
            'code' : 200,
            'message' : '사용자 찾음',
            'data' : {
                'user' : found_user.get_data_object()
            }
        }
    
    else :   
        return {
            'code' : 400,
            'message' : '해당 이메일의 사용자 없음',
        }, 400