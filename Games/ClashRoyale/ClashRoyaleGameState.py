from Core.GameState import GameState
from ClashRoyaleTower import ClashRoyaleTower
from ClashRoyaleCard import ClashRoyaleCard
from Games.ClashRoyale.ClahsRoyaleCardCollection import ClashRoyaleCardCollection
from Games.ClashRoyale.ClashRoyaleBoard import ClashRoyaleBoard
from Games.ClashRoyale.ClashRoyaleObservation import ClashRoyaleObservation


class ClashRoyaleGameState(GameState):
    def __init__(self):
        self.deck_p1 = ClashRoyaleCardCollection()
        self.deck_p2 = ClashRoyaleCardCollection()

        self.units_p1 = []
        self.units_p2 = []

        self.hand_p1 = ClashRoyaleCardCollection()
        self.hand_p2 = ClashRoyaleCardCollection()

        self.towers_p1 = [ClashRoyaleTower(), ClashRoyaleTower(), ClashRoyaleTower()]
        self.towers_p2 = [ClashRoyaleTower(), ClashRoyaleTower(), ClashRoyaleTower()]

        self.elixir_p1 = 7
        self.elixir_p2 = 7

        self.time = 180
        self.board = ClashRoyaleBoard(29, 19)  # rows x columns

        self.winner = -1  # -1 no hay ganador, 1 el p1 ha ganado, 2 el p2 ha ganado
        self.turn = 0

    def reset(self, player_id_as_first):
        self.turn = player_id_as_first
        self.winner = -1
        self.elixir_p1 = 7
        self.elixir_p2 = 7
        self.time = 180

        self.init_deck(self.deck_p1)
        self.init_deck(self.deck_p2)

        self.init_hand(self.deck_p1, self.hand_p1)
        self.init_hand(self.deck_p2, self.hand_p2)

        self.towers_p1 = [ClashRoyaleTower(), ClashRoyaleTower(), ClashRoyaleTower()]
        self.towers_p2 = [ClashRoyaleTower(), ClashRoyaleTower(), ClashRoyaleTower()]

        self.board = ClashRoyaleBoard(29, 19) # rows x columns

    # Create cards, add to deck and shuffle it
    def init_deck(self, deck):
        deck.clear()
        for i in range(8):
            deck.add_card(ClashRoyaleCard())
        deck.shuffle()

    # Repeat 4 times: draw a card from the deck, add to the hand and append again (at the end) to the deck
    def init_hand(self, deck, hand):
        hand.clear()
        for i in range(4):
            card = deck.draw()
            hand.add_card(card)
            deck.add_card(card)

    def is_terminal(self):
        if self.winner != -1:
            return True
        else:
            return False

    def get_observation(self):
        # TODO: hay que completarlo
        obs = ClashRoyaleObservation(self.turn, self.hand_p1, self.hand_p1, self.elixir_p1, self.elixir_p2)
        return obs

    def __str__(self):
        s = "Turn: " + str(self.turn) + "\n"
        s += "Time: " + str(self.time) + "\n"
        s += "Board:" + "\n"
        s += str(self.board) + "\n"

        s += "Player 1 hand:   "
        s += str(self.hand_p1) + "\n"
        s += "Player 2 hand:   "
        s += str(self.hand_p2) + "\n"

        s += "Player 1 deck:   "
        s += str(self.deck_p1) + "\n"
        s += "Player 2 deck:   "
        s += str(self.deck_p2) + "\n"

        s += "Player 1 towers: "
        for t in self.towers_p1:
            s += str(t) + " "
        s += "\n"
        s += "Player 2 towers :"
        for t in self.towers_p2:
            s += str(t) + " "
        s += "\n"

        return s


'''
        symbolP1Units = ["1", "2", "3", "4", "5", "6", "7", "8"]
        symbolP2Units = ["A", "B", "C", "D", "E", "F", "G", "H"]

        symbolTorre = "*"
        symbolAgua = "="
        symbolSuelo = " "

        resultado = "Las unidades del jugador 1 se mostraran con numeros del 1 al 8 \n"
        resultado += "Las unidades del jugador 2 con letras de la A a la H \n\n"

        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                # ver las unidades del p1
                for x in range(len(self.units_p1)):
                    if self.units_p1[x].pos_x == i and self.units_p1[x].pos_y == j:
                        resultado += symbolP1Units[x]

                # ver las unidades del p2
                for x in range(len(self.units_p2)):
                    if self.units_p2[x].pos_x == i and self.units_p2[x].pos_y == j:
                        resultado += symbolP2Units[x]

                # ver si estamos en alguna torre, se que todo podria estar en una linea pero asi es mas legible
                if 2 <= i <= 4 and 3 <= j <= 5:  # Torre arriba izq
                    resultado += symbolTorre

                elif 7 <= i <= 10 and 0 <= j <= 3:  # Torre arriba medio
                    resultado += symbolTorre

                elif 13 <= i <= 15 and 3 <= j <= 5:  # Torre arriba der
                    resultado += symbolTorre

                elif 2 <= i <= 4 and 24 <= j <= 26:  # Torre abajo izq
                    resultado += symbolTorre

                elif 7 <= i <= 10 and 25 <= j <= 28:  # Torre abajo medio
                    resultado += symbolTorre

                elif 13 <= i <= 15 and 24 <= j <= 26:  # Torre abajo der
                    resultado += symbolTorre

                elif i != 3 and i != 14 and j == 14:  # rio
                    resultado += symbolAgua
                else:
                    resultado += symbolSuelo
        resultado += "\n\n"

        # ya hemos imprimido el mapa
        # ahora los datos

        # torres del p1
        resultado += "T1 "
        for torre in self.towers_p1:
            resultado += str(torre.health) + " "
        resultado += "\n"

        # torres del p2
        resultado += "T2 "
        for torre in self.towers_p2:
            resultado += str(torre.health) + " "
        resultado += "\n"

        # unidades del p1
        for i in range(len(self.units_p1)):
            resultado += symbolP1Units[i] + str(self.units_p1[i].health) + "\n"
        resultado += "\n"

        # unidades del p2
        for i in range(len(self.units_p2)):
            resultado += symbolP2Units[i] + str(self.units_p2[i].health) + "\n"
        resultado += "\n"

        # mano del p1
        resultado += "Mano del P1:\n"
        for carta in self.hand_p1.get_cards():
            resultado += carta.tipo + " " + carta.coste
        resultado += "\n"

        # mano del p2
        resultado += "Mano del P2:\n"
        for carta in self.hand_p2.get_cards():
            resultado += carta.tipo + " " + carta.coste
        resultado += "\n"

        # mazo del p1
        resultado += "Mazo del P1:\n"
        for carta in self.deck_p1:
            resultado += carta.tipo + " " + carta.coste
        resultado += "\n"

        # mazo del p2
        resultado += "Mazo del P2:\n"
        for carta in self.deck_p2:
            resultado += carta.tipo + " " + carta.coste
        resultado += "\n"

        # elixir de ambos
        resultado += "Elixir del P1: " + str(self.elixir_p1) + "\n"
        resultado += "Elixir del P2: " + str(self.elixir_p2) + "\n"
'''