from cell import cell

class board:
    def __init__(self,capacity:int) -> None:
        self.size = capacity
        self.cells = [cell(i) for i in range(1,capacity+1)]
    
    def make_cell_snake_or_ladder(self,start:int,end:int):
        snake_or_ladder_cell = self.cells[start]
        snake_or_ladder_cell.to = end
    
    
    def get_new_position_after_snake_or_ladder(self, position):

        return self.cells[position].to