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
        
        
    # 리뷰를 등록하기 전에, 이미 리뷰썼다면 못쓰게 막자
    sql = f"SELECT * FROM lecture_review WHERE lecture_id={params['lecture_id']} AND user_id={params['user_id']}" 
      
    already_write_review_result = db.executeOne(sql)
    
    if already_write_review_result:
        return {
            'code' : 400,
            'message' : '이미 리뷰 썼자나!'
        }, 400
           
        
    # 실제 리뷰 등록
    sql = f"""
    INSERT INTO lecture_review 
    (lecture_id, user_id, title, content, score) 
    VALUES 
    ({params['lecture_id']},{params['user_id']},'{params['title']}','{params['content']}', {score}) 
    """
    
    return{
        'code' : 200,
        'message' : '리뷰 등록 성공'
    }
    
    
# 강의 수정하는 기능
def modify_review(params):
    
    # 파라미터 정리 
    # field : 어느 항목을 바꿀 지 알려주는 역할
    # value : 해당 항목에 실제로 넣어줄 값
    # user_id : 변경을 시도하는 사람이 누구인지?
    # review_id : 변경해줄 리뷰의 id
    
    column_name = params['field']
    
    # 파라미터 검증을 해보자
    # 검증 0 : 받아온 리뷰 아이디에 해당하는 리뷰가 실존해?
    sql = f"SELECT * FROM lecture_review WHERE id={params['review_id']}"
    
    review_data = db.executeOne(sql)
    
    if review_data == None:
        return{
            'code' : 400,
            'message' : '해당 리뷰는 존재하지 않습니다.'    
        }, 400
    
    
    
    #1. 제목 변경
    if column_name == 'title':
        sql = f"UPDATE lecture_review SET title = '{params['value']}' WHERE id = {params['review_id']}"
        
        db.cursor.execute(sql)
        db.db.commit()
        
        return {
            'code' : 200,
            'message' : '제목을 수정했습니다.',
        }
    
    #2. 내용 변경
    if column_name == 'content':
        sql = f"UPDATE lecture_review SET content='{params['value']}' WHERE id = {params['review_id']}"
        db.cursor.execute(sql)
        db.db.commit()

        return {
            'code': 200,
            'message': '내용을 수정했습니다.'
        }
        
    #3. 점수 변경
    if column_name == 'score':
        sql = f"UPDATE lecture_review SET score={params['value']} WHERE id = {params['review_id']}"

        db.cursor.execute(sql)
        db.db.commit()

        return {
            'code': 200,
            'message': '점수를 수정했습니다.'
        }
   
    # 여기까지 내려왔다? field 파라미터에 잘못된값이 들어갔으므로 -> 수정 분기로 들어가지 않았다.
    return {
        'code': 400,
        'message': 'field에 잘못된 값이 입력되었습니다.'
    }, 400 
