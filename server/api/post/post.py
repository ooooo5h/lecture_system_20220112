from server import db
from server.model import Posts

# 모든 게시글 조회
def get_all_posts(params):
    
    sql = f"SELECT * FROM posts ORDER BY created_at DESC"
    
    post_data_list = db.executeAll(sql)
    
    post_list = [Posts(row).get_data_object()  for row in post_data_list]
    
    return {
        'code' : 200,
        'message' : '모든 게시글 조회',
        'data' : {
            'posts' : post_list,
        }
    }
    
    
# 특정 게시글 상세 조회 : GET /post/5
def view_post(post_id, params):
    return {
        '임시' : '특정 게시글 상세 조회',
    }
    
    
# 게시글 등록
def add_post(params):
    return {
        '임시' : '게시글 등록',
    }
    
    
# 게시글 수정
def modify_post(params):
    return {
        '임시' : '게시글 수정',
    }
    
    
# 게시글 삭제
def delete_post(params):
    return {
        '임시' : '게시글 삭제',
    }