from Core.GameState import GameState
from Games.ClashRoyale.ClashRoyaleObservation import ClashRoyaleObservation


class ClashRoyaleGameState(GameState):
    def __init__(self, deck_p1, deck_p2, base_tower, time, board_width, board_height):
        self.deck_p1 = deck_p1
        self.deck_p2 = deck_p2

        self.units_p1 = []  # al principio no tienen unidades en el campo
        self.units_p2 = []

        self.hand_p1 = [deck_p1[0], deck_p1[1], deck_p1[2], deck_p1[3]]  # se debería hacer aleatorio el inicio
        self.hand_p2 = [deck_p2[0], deck_p2[1], deck_p2[2], deck_p2[3]]

        self.towers_p1 = [base_tower, base_tower, base_tower]
        self.towers_p2 = [base_tower, base_tower, base_tower]

        self.elixir_p1 = 0
        self.elixir_p2 = 0

        self.time = time
        self.board = []

        for i in range(board_width):
            fila = []
            for j in range(board_height):
                fila.append(0)
            self.board.append(fila)

        self.winner = -1  # -1 no hay ganador, 1 el p1 ha ganado, 2 el p2 ha ganado

    def reset_game(self):
        pass

    def is_terminal(self):
        if self.winner != -1:
            return True
        else:
            return False

    def get_observation(self):
        obs = ClashRoyaleObservation(self.deck_p1, self.elixir_p1, self.winner)
        return obs

    def __str__(self):
        s = "player 1 towers are: " + self.towers_p1[0] + " " + self.towers_p1[1] + " " + self.towers_p1[2] + "\n"
        s += "player 1 elixir is: " + "\n"
        s += "player 1 hand is: " + self.hand_p1[0] + self.hand_p1[1] + self.hand_p1[2] + self.hand_p1[3] + "\n"
        s += "and player 1 deck is: " + self.deck_p1[0] + self.deck_p1[1] + self.deck_p1[2] + \
             self.deck_p1[3] + self.deck_p1[4] + self.deck_p1[5] + self.deck_p1[6] + self.deck_p1[7] + "\n\n"

        s += "player 2 towers are: " + self.towers_p2[0] + " " + self.towers_p2[1] + " " + self.towers_p2[2] + "\n"
        s += "player 2 elixir is: " + "\n"
        s += "player 2 hand is: " + self.hand_p2[0] + self.hand_p2[1] + self.hand_p2[2] + self.hand_p2[3] + "\n"
        s += "and player 2 deck is: " + self.deck_p2[0] + self.deck_p2[1] + self.deck_p2[2]\
             + self.deck_p2[3] + self.deck_p2[4] + self.deck_p2[5] + self.deck_p2[6] + self.deck_p2[7]