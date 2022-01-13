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
    
# 리뷰 수정하는 기능(특정 항목을 지정해서 해당 항목만 수정 : 부분수정)
def modify_review(params):
    
    # 파라미터 정리
    # field : 어느 항목을 바꿀지 알려주는 역할
    # value : 해당 항목에 실제로 넣어줄 값
    # user_id : 변경을 시도하는 사람이 누구인지 고유 번호
    # review_id : 변경해줄 리뷰의 id
    
    # field라는 이름표로, 어느 항목을 바꾸고 싶은지 그 자체를 받아오자
    column_name = params['field']
    
    # 제목 변경하구 싶니?
    if column_name == 'title':
        sql = f"UPDATE lecture_review SET title='{params['value']}' WHERE id = {params['review_id']} "
    
        # DB에 변경이 발생했으니 쿼리실행 및 commit이 필요함
        db.cursor.execute(sql)
        db.db.commit()
        
        # 제목 변경 성공으로 리턴
        return {
            'code' : 200,
            'message' : '제목 수정 성공'
        }
        
        
    # 내용 변경
    if column_name == 'content':
        sql = f"UPDATE lecture_review SET content='{params['value']}' WHERE id = {params['review_id']}"
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return {
            'code' : 200,
            'message' : '내용 수정 성공',
        }
    
    
    # 점수 변경
    if column_name == 'score':
        sql = f"UPDATE lecture_review SET score='{params['value']}' WHERE id = {params['review_id']}"
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return {
            'code' : 200,
            'message' : '점수 수정 성공',
        }       
    
    # 여기까지 왔다는 건, field에 잘못된 값이 들어와서 수정하는 if문으로 못들어갔다     
    return {
        'code' : 400,
        'message' : '임마 필드에 값 잘못입력했어',
    }, 400