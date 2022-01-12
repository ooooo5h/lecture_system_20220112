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