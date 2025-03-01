
import threading
from game import game

class gameManager:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        raise RuntimeError("this is singleton class, invoke get_instance() instead")
    
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = cls.__new__(cls)
                return cls._instance
    
    def start_new_game(self,id,player_names,board_size,KsidedDice):
        new_game = game(id,player_names,board_size,KsidedDice)
        threading.Thread(target=new_game.play).start()

