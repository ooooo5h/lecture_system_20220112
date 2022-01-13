from turtle import screensize
from server import db

def write_review(params):
    
    # 1. 평점은 1~5 사이로만 가능.
    score = float(params['score'])
    
    if not ( 1<= score <= 5):
        return {
            'code' : 400,
            'message' : '1~5사이 평점 입력'
        }, 400

    # 2. 제목의 길이는 최소 5자 이상.    
    if len(params['title']) < 5:
        return {
            'code' : 400,
            'message' : '제목 길이 5자 이상'
        }, 400
    
    # 3. 내용의 길이는 최소 10자 이상.
    if len(params['content']) < 10:
        return {
        'code' : 400,
        'message' : '내용 길이 10자 이상'
    }, 400

    # DB내부 조회 결과 활용
    # 4. 수강을 했어야만 리뷰 작성 가능.
    sql = f"SELECT * FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    apply_class_result = db.executeOne(sql)
    
    if not apply_class_result:
        return {
            'code' : 400,
            'message' : '수강신청해야지 리뷰 쓸 수 있다',
        }