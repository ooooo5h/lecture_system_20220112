class Posts:
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.title = data_dict['title']
        self.content = data_dict['content']
        self.created_at = data_dict['created_at']
        
    def get_data_object(self):
        
        data = {
            'id' : self.id,   
            'user_id' : self.user_id,
            'title' : self.title,
            'content' : self.content,
            'created_at' : str(self.created_at),
        }
        
        return data