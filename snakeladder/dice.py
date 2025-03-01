import random
class dice:
    def __init__(self,no_of_sides) -> None:
        self.sides=no_of_sides
    
    def roll(self):
        return random.randint(1,self.sides)