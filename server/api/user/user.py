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
    
    # 도전과제 : 이메일이 중복이면 가입 불허할 예정
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    already_user_data = db.executeOne(sql)
    
    # 이미 가입한 사람이 있다면 400으로 중복처리
    if already_user_data :
        return {
            'code' : 400,
            'message' : '이미 사용중인 이메일',
        }, 400
    
    sql = f"INSERT INTO users (email, password, name) VALUES ('{params['email']}', '{params['pw']}', '{params['name']}')"
    
    db.insetAndCommit(sql)
    
    return {
        'code' : 200,
        'message' : '회원가입 성공',
    }

# 이메일을 받아서 사용자 정보를 조회하는 기능
def find_user_by_email(params):
    
    sql = f"SELECT * FROM users WHERE email = '{params['email']}'"
    
    find_user_data = db.executeOne(sql)
    
    if find_user_data :
        # 해당 이메일의 사용자가 발견된 경우
        
        find_user = Users(find_user_data)
        
        return {
            'code' : 200,
            'message' : '사용자를 찾았음',
            'data' : {
                'user' : find_user.get_data_object()
            }
        }
        
    else :
        # 검색되지 않은 경우
        return {
            'code' : 400,
            'message' : '해당 사용자 없음',
        }, 400