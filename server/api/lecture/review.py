from server import db

# 강의의 리뷰에 대한 기능한 모아두는 별도의 파이썬 파일

def write_review(params):
    
    # 1 : 평점은 1~5점 사이로만 가능
    # 파라미터들은 기본적으로 str형태로 들어오기 때문에, float로 먼저 변환해두고 사용하자   
    score = float(params['score'])   
    if not (1 <= score <= 5):
        return {
            'code' : 400,
            'message' : '평점은 1 ~ 5점 사이여야 합니다.'
        }, 400
    
    # 2 : 제목의 길이는 최소 5글자 이상
    # => str의 길이, 파라미터 자체의 길이를 체크하면 됨    
    if len(params['title']) < 5 :
        return {
            'code' : 400,
            'message' : '제목은 최소 5글자 이상 입력하세요.',
        }, 400
      
    # 3 : 내용의 길이는 최소 10자 이상
    if len(params['content']) < 10 :
        return {
        'code' : 400,
        'message' : '내용은 최소 10글자 이상 입력하세요.',
    }, 400
    

    # 4 : 수강을 했어야지만 리뷰 작성 가능 
    # ( DB 내부 조회 결과 활용)
    sql = f"SELECT * FROM lecture_user WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"
    
    query_result = db.executeOne(sql)
    
    if not query_result :
        # 수강 신청 안해놓고 리뷰 작성하려는 케이스
        return {
            'code' : 400,
            'message' : '수강신청부터 하렴. 수강신청 안해서 리뷰작성 모태'
        }, 400        
        
    # 5 : 이미 리뷰를 작성했다면, 추가 리뷰 작성 불가하게 막자
    sql = f"SELECT * FROM lecture_review WHERE lecture_id = {params['lecture_id']} AND user_id = {params['user_id']}"    
        
    already_write_review = db.executeOne(sql)
    
    if already_write_review :
        return {
            'code' : 400,
            'message' : '이미 작성했으면 또 작성 모태',
        }, 400   
    
    # 리뷰 실제 등록
    sql = f"""
    INSERT INTO lecture_review
    (lecture_id, user_id, title, content, score)
    VALUES ({params['lecture_id']}, {params['user_id']}, '{params['title']}', '{params['content']}', {params['score']})
    """
    
    db.insertAndCommit(sql)
    
    return {
        'code' : 200,
        'message' : '리뷰 등록 성공!',
    }
    
# 리뷰 수정하는 기능
def modify_review(params):
    return {
        '임시' : '리뷰 수정 기능 테스트'
    }