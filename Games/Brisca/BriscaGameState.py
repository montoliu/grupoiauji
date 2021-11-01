from Core.GameState import GameState
from Games.Brisca.BriscaDeck import BriscaDeck


class BriscaGameState(GameState):
    def __init__(self):
        self.main_deck = BriscaDeck()
        self.l_hands = []
        self.main_type = None
        self.l_won_cards = []
        self.turn = 0

    def get_observation(self):
        pass

    def is_terminal(self):
        pass
