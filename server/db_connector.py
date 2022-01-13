import pymysql
from pymysql.cursors import DictCursor

class DBConnector:
    
    def __init__(self):
        self.db = pymysql.connect(
            host='finalproject.cbqjwimiu76h.ap-northeast-2.rds.amazonaws.com',
            port=3306,
            user='admin',
            passwd='Vmfhwprxm!123',
            db='test_202112_python',
            charset = 'utf8',  
            cursorclass = DictCursor,
        )
        
        self.cursor = self.db.cursor()
        
    
    # 쿼리를 실행하고, 그에 대한 목록을 리턴하는 메쏘드 추가
    def executeAll(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    
    # 쿼리를 실행하고, 한 줄만 리턴하는 메쏘드 추가
    def executeOne(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    
    # 하나의 데이터를 추가/변경/삭제 등 DB에 영향주는 쿼리를 실행하고, 바로 DB에 기록하는 메쏘드 추가
    def executeQueryAndCommit(self, sql):
        self.cursor.execute(sql)
        self.db.commit()    # return이 없는 이유? commit()은 결과값 자체가 없어서 return을 안해도 함수가 끝남