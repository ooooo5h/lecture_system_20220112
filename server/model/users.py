class Users:
    
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.email = data_dict['email']
        self.name = data_dict['name']
        self.birth_year = data_dict['birth_year']
        self.address = data_dict['address']
        self.gender = data_dict['gender']
        
    
    # 필요한 모양에 맞게 가공하는 함수
    def get_data_object(self):
        
        data = {
            'id' : self.id,
            'email' : self.email,
            'name' : self.name,
            'birth_year' : self.birth_year,
            'address' : self.address,
            'gender' : self.gender,
        }
        
        return data