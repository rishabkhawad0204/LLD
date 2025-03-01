from board import board
from dice import dice
from player import player

class game:
    def __init__(self,id,players,board_size,KsidedDice) -> None:
        self.game_id = id
        self.players = [player(player_name,clr) for player_name,clr in players]
        self.board = board(board_size)
        self.dice = dice(KsidedDice)
        self.current_player_index = 0
    
    def _initialise_snakes_and_ladders(self):

        self.board.make_cell_snake_or_ladder(20,5)
        self.board.make_cell_snake_or_ladder(28,12)
        self.board.make_cell_snake_or_ladder(20,100)
    
    def play(self):
        while not self._is_game_over():
            current_player = self.players[self.current_player_index]
            dice_roll = self.dice.roll()
            new_position = current_player.position + dice_roll

            if new_position <= self.board.size:
                current_player.position = self.board.get_new_position_after_snake_or_ladder(new_position)
                print(f"{current_player.player_name} rolled a {dice_roll} and moved to position {current_player.position}")
            else:
                print(f"{current_player.player_name} rolled a {dice_roll} which is greater than board size, so turn skipped")
            if current_player.position == self.board.size:
                print(f"{current_player.player_name} wins!")
                break

            self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def _is_game_over(self):
        for player in self.players:
            if player.position == self.board.size:
                return True
        return False

    