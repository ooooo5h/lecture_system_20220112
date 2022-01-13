from server.model import Lectures, Reviews
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
    
    # 같은 과목에 같은사람이 신청은 불가
    
    sql = f"SELECT * FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    already_apply_result = db.executeOne(sql)
    
    if already_apply_result :
        return {
            'code' : 400,
            'message' : '이미 신청한 과목 또 신청 노놉'
        }, 400
    
    # 틀린 부분 :: INSERT INTO 는 VALUES 하고 (값)  >> WHERE절 XX
    # sql = f"INSERT INTO lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    sql = f"INSERT INTO lecture_user VALUES ({params['lecture_id']} ,{params['user_id']})"
    
    db.insertAndCommit(sql)
    
    return{
        'code' : 200,
        'message' : '수강신청 성공'
    }
    
    
# 수강 취소 기능
def cancel_apply(params):
    
    # 수강 신청 안한 과목은 취소 불가 400 처리
    sql =f"SELECT * FROM lecture_user WHERE user_id = {params['user_id']} AND lecture_id = {params['lecture_id']}"
    
    already_apply_lecture_result = db.executeOne(sql)
    
    if not already_apply_lecture_result:
        return {
            'code' : 400,
            'message' : '수강 신청 안한 과목은 취소 불가'
        }, 400  
    
    # 실제 신청 내역 삭제. (쿼리 매우 유의)
    sql = f"DELETE FROM lecture_user WHERE user_id = {params['user_id']} AND lecture_id = {params['lecture_id']} "
    
    db.cursor.execute(sql)
    db.db.commit()
    
    return {
        'code' : 200,
        'message' : '수강 취소 성공'
    }
    

# 특정 강의 상세보기
def view_lecture_detail(id, params):
    
    # 1. 강의 자체에 대한 정보 조회
    sql = f"SELECT * FROM lectures WHERE id = {id}"
    
    lecture_data = db.executeOne(sql)
    lecture = Lectures(lecture_data)
    
    
    # 2. 모든 리뷰 내역을 추가로 첨부.
    sql = f"SELECT * FROM lecture_review WHERE lecture_id = {id}"
    
    review_data_list = db.executeAll(sql)
    review_list = [Reviews(row).get_data_object() for row in review_data_list]
     
    
    # 3. 강의의 평점을 추가로 조회 (해당 강의의 모든 리뷰의 점수 -> 평균)

    
    
    return{
        'code' : 200,
        'message' : '강의 상세 조회',
        'data' : {
            'lecture' : lecture.get_data_object(reviews=review_list),
        }
    }