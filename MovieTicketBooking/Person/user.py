from .person import Iperson

class user(Iperson):

    def __init__(self,id,name,email_id):
        self._id = id
        self._name = name
        self._email_id = email_id
        self.bookings = {}
    
    def get_name(self):
        return print(f"username is {self.name}")


    @property
    def name(self):
        return self._name
    
    @property
    def email_id(self):
        return self._email_id
    
    @property
    def id(self):
        return self._id
    
    

    
    


    

        