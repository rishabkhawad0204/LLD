import uuid

class theater:
    def __init__(self,id,name,theatre_coord) -> None:
        self.id = id
        self.name = name
        self.location = theatre_coord
        self.halls = {}
        self.movie_shows = {}