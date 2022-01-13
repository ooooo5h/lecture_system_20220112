class Reviews:
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.lecture_id = data_dict['lecture_id']
        self.user_id = data_dict['user_id']
        self.title = data_dict['title']
        self.content = data_dict['content']
        self.score = data_dict['score']
        self.created_at = data_dict['created_at']        
        
    def get_data_object(self):
        data = {
            'id': self.id,
            'lecture_id': self.lecture_id,
            'user_id': self.user_id,
            'title': self.title,
            'content': self.content,
            'score': self.score,
            'created_at': str(self.created_at),
            }
        
        return data