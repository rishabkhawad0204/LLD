from game_manager import gameManager

class SnakeAndLadderDemo:
    def run():
        game_manager = gameManager.get_instance()

        # Start game 1
        players1 = [("Player 1","red"), ("Player 2","green"), ("Player 3","yellow")]
        game_manager.start_new_game(1,players1,100,6)

        # Start game 2
        # players2 = [("Player 1","blue"), ("Player 2","pink"), ("Player 3","orange")]
        # game_manager.start_new_game(1,players2,100,6)

if __name__ == "__main__":
    SnakeAndLadderDemo.run()