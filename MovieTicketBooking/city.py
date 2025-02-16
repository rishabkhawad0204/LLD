import uuid
class city:
    def __init__(self,id,name,state) -> None:
        self.id = id
        self.name = name
        self.state = state
        self.theaters = {}