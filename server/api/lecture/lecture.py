from server.model import Lectures, Reviews
from server import db

def get_all_lecture(params):
    # 모든 강의 목록을 <이름순으로> 내려주자 => 당장은 params 변수 활용 X
    
    sql = f"SELECT * FROM lectures ORDER BY name"
    
    db_list = db.executeAll(sql)
    
    lectures = [ Lectures(row).get_data_object() for row in db_list ]
    
    return {
        'code' : 200,
        'message' : '모든 강의 목록 조회',
        'data' : {
            'lectures' : lectures,
        }
    }
    

# 수강신청 기능
def apply_lecture(params):
    
    # 같은 과목에 같은 사람이 신청하는 건 노놉!! (SELECT)
    sql = f"SELECT * FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    already_apply = db.executeOne(sql)
    
    if already_apply :
        return {
            'code' : 400,
            'message' : '이미 신청했잖아 노놉!!'
        }, 400   
    
    # lecture_user 테이블에 한 줄 추가 (INSERT INTO)
    
    sql = f"INSERT INTO lecture_user VALUES ({params['lecture_id']}, {params['user_id']})"
    
    db.insertAndCommit(sql)
    
    return {
        'code' : 200,
        'message' : '수강 신청을 성공!',
    }
    

# 수강 취소 기능
def cancel_apply(params):
    
    # 1. 수강 신청 안한 과목을 취소하면 400 리턴
    sql = f"SELECT * FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    already_apply = db.executeOne(sql)
    
    if not already_apply :
        return {
            'code' : 400,
            'message' : '수강 신청 내역이 없습니다.'
        }, 400
    
    #향후 - 토큰값을 받아내서 내가 신청한 과목만 취소 가능하도록 만들거야(later)

    
    # 2. 실제 신청 내역 삭제 (DELETE는 항상 쿼리 매우 유의!!)
    sql = f"DELETE FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    # DELETE문도 쿼리실행하고 DB변경을 확정짓는 절차로, INSERT INTO와 동일하게 동작된다
    db.cursor.execute(sql)
    db.db.commit()

    return {
        'code' : 200,
        'messsage' : '수강 취소 완료',
    }
    
    
# 특정 강의 상세보기
def view_lecture_detail(id, params):
    
    # 1 : 강의 자체에 대한 정보 조회
    sql = f"SELECT * FROM lectures WHERE id = {id}"
    
    lecture_data = db.executeOne(sql)
    
    lecture = Lectures(lecture_data)
    
    # 2 : 모든 리뷰 내역을 추가로 첨부
    sql = f"SELECT * FROM lecture_review WHERE lecture_id = {id}"
    
    review_data_list = db.executeAll(sql)
    
    review_list = [ Reviews(row).get_data_object()  for row in review_data_list]
    
    
    
    # 3 : 강의에 대한 모든 리뷰 점수의 평균을 추가로 조회
    
    return {
        'code' : 200,
        'message' : '강의 상세 조회',
        'data' : {
            'lecture' : lecture.get_data_object(reviews = review_list)   # data안에있는 lecture가 reviews를 들고 있게끔 변경
        }
    }
