class Lectures:
    
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.max_count = data_dict['max_count']
        self.fee = data_dict['fee']
        self.campus = data_dict['campus']


    # 리뷰 목록이 추가된다면 강의의 하위 데이터로 reviews:[]를 추가해보자
    # 기본값 : None => 리뷰를 다루지 않는 경우(전체 강의 목록 불러내기)도 대응하기 위해서        
    def get_data_object(self, reviews=None):    
        
        # data { } => dict를 만드는 행위    
        
        data = {
            'id' : self.id,
            'name' : self.name,
            'max_count' : self.max_count,
            'fee' : self.fee,
            'campus' : self.campus,            
        }
        
        # dict에는 키를 새로 지정해서 새 변수를 추가하는 것도 가능
        # 만약에 reviews 파라미터에 실제 데이터가 들어왔다면, 추가해주자
        if reviews :
            data['reviews'] = reviews
                
        return data