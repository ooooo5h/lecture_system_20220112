from server.model import Lectures
from server import db


# 모든 강의 목록 <이름순으로> 내려주기
def get_all_lectures(params):
    
    sql = "SELECT * FROM lectures ORDER BY name"
    
    lecture_list = db.executeAll(sql)
    
    lectures = [Lectures(row).get_data_object()  for row in lecture_list]
    
    return {
        'code' : 200,
        'message' : '모든 강의 목록 이름순으로 정렬 및 불러오기',
        'data' : {
            'lectures' : lectures,
        }
    }
    
# 수강 신청 기능
def apply_lecture(params):
    return{
        '임시' : '수강신청 테스트',
    }