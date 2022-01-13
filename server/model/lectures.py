from audioop import avg


class Lectures:
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.max_count = data_dict['max_count']
        self.fee = data_dict['fee']
        self.campus = data_dict['campus']

        
    def get_data_object(self, reviews=None):        
        
        data = {
            'id' : self.id,
            'name' : self.name,
            'max_count' : self.max_count,
            'fee' : self.fee,
            'campus' : self.campus,            
        }
         
        if reviews :
            data['reviews'] = reviews
            
            sum_score = 0
            
            for review in reviews:
                sum_score += review['score']

            avg_score = sum_score / len(reviews)          
            
            data['avg_score'] = avg_score  
            
        
        return data