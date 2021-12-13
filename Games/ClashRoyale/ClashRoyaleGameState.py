from Core.GameState import GameState


class ClashRoyaleGameState(GameState):
    def __init__(self, deck_p1, deck_p2, base_tower, elixir_p1, elixir_p2):
        self.deck_p1 = deck_p1  #clase cardCollection
        self.deck_p2 = deck_p2

        self.units_p1 = []  # al principio no tienen unidades en el campo
        self.units_p2 = []

        self.hand_p1 = [deck_p1[0], deck_p1[1], deck_p1[2], deck_p1[3]]  # se debería hacer aleatorio el inicio
        self.hand_p2 = [deck_p2[0], deck_p2[1], deck_p2[2], deck_p2[3]]

        self.towers_p1 = [base_tower, base_tower, base_tower]
        self.towers_p2 = [base_tower, base_tower, base_tower]

        self.elixir_p1 = elixir_p1
        self.elixir_p2 = elixir_p2

        self.time = 180
        self.board = []

    # mapa 29 x 18
        self.board_height = 29
        self.board_width = 18
        for i in range(self.board_width):
            fila = []
            for j in range(self.board_height):
                fila.append(0)
            self.board.append(fila)

        self.winner = -1  # -1 no hay ganador, 1 el p1 ha ganado, 2 el p2 ha ganado

    def reset_game(self):
        self.time = 180
        self.elixir_p1 = 7
        self.elixir_p2 = 7
        for i in range(self.board_width):
            fila = []
            for j in range(self.board_height):
                fila.append(0)
            self.board.append(fila)
        self.deck_p1.clear
        self.deck_p2.clear
        self.units_p1 = []
        self.units_p2 = []
        self.winner = -1


    def is_terminal(self):
        if self.winner != -1:
            return True
        else:
            return False

    def get_observation(self):
        obs = ClashRoyaleObservation(self.deck_p1, self.elixir_p1, self.winner)
        return obs

    #def __str__(self):
    #    s = "player 1 towers are: " + self.towers_p1[0] + " " + self.towers_p1[1] + " " + self.towers_p1[2] + "\n"
    #    s += "player 1 elixir is: " + "\n"
    #    s += "player 1 hand is: " + self.hand_p1[0] + self.hand_p1[1] + self.hand_p1[2] + self.hand_p1[3] + "\n"
    #    s += "and player 1 deck is: " + self.deck_p1[0] + self.deck_p1[1] + self.deck_p1[2] + \
    #         self.deck_p1[3] + self.deck_p1[4] + self.deck_p1[5] + self.deck_p1[6] + self.deck_p1[7] + "\n\n"

    #    s += "player 2 towers are: " + self.towers_p2[0] + " " + self.towers_p2[1] + " " + self.towers_p2[2] + "\n"
    #    s += "player 2 elixir is: " + "\n"
    #    s += "player 2 hand is: " + self.hand_p2[0] + self.hand_p2[1] + self.hand_p2[2] + self.hand_p2[3] + "\n"
    #    s += "and player 2 deck is: " + self.deck_p2[0] + self.deck_p2[1] + self.deck_p2[2]\
    #         + self.deck_p2[3] + self.deck_p2[4] + self.deck_p2[5] + self.deck_p2[6] + self.deck_p2[7]


    def __str__(self):
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
            resultado += str(torre.vida) + " "
        resultado += "\n"

        # torres del p2
        resultado += "T2 "
        for torre in self.towers_p2:
            resultado += str(torre.vida) + " "
        resultado += "\n"

        # unidades del p1
        for i in range(len(self.units_p1)):
            resultado += symbolP1Units[i] + str(self.units_p1[i].vida) + "\n"
        resultado += "\n"

        # unidades del p2
        for i in range(len(self.units_p2)):
            resultado += symbolP2Units[i] + str(self.units_p2[i].vida) + "\n"
        resultado += "\n"

        # mano del p1
        resultado += "Mano del P1:\n"
        for carta in self.hand_p1:
            resultado += carta.tipo + " " + carta.coste
        resultado += "\n"

        # mano del p2
        resultado += "Mano del P2:\n"
        for carta in self.hand_p2:
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