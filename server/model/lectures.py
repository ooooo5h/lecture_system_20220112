class Lectures:
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.max_count = data_dict['max_count']
        self.fee = data_dict['fee']
        self.campus = data_dict['campus']

        
    def get_data_object(self):        
        
        data = {
            'id' : self.id,
            'name' : self.name,
            'max_count' : self.max_count,
            'fee' : self.fee,
            'campus' : self.campus,            
        }
        
        return data