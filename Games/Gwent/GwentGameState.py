import random

from Core.GameState import GameState
from Games.Gwent.GwentCardCollection import GwentCardCollection


class GwentGameState(GameState):

    def __init__(self):
        self.players = 2
        self.lives_p1 = 3
        self.lives_p2 = 3
        self.points_p1 = 0
        self.points_p2 = 0
        self.randomized_main_deck_0 = GwentCardCollection()
        self.randomized_main_deck_1 = GwentCardCollection()
        self.hands = []
        self.terrain_p1 = []
        self.terrain_p2 = []
        self.turn = 0
        self.winner = -1

    def get_observation(self):
        list_all_cards = []
        list_all_cards.extend(self.main_deck.get_cards())
        for p in range(self.players):
            if p != self.turn:
                list_all_cards.extend(self.hands[p].get_cards())

        random.shuffle(list_all_cards)

        randomized_main_deck_0 = GwentCardCollection()
        randomized_main_deck_0.add_cards(list_all_cards)
        randomized_main_deck_1 = GwentCardCollection()
        randomized_main_deck_1.add_cards(list_all_cards)
        randomized_hands = []

        for p in range(self.players):
            randomized_hands.append(GwentCardCollection())
            n = self.hands[p].len()
            if p != self.turn:
                for i in range(n):
                    card = randomized_main_deck_0.draw()
                    randomized_hands[p].add_card(card)
            else:
                for i in range(n):
                    card = randomized_main_deck_1.draw()
                    randomized_hands[p].add_card(card)

        #Queda implementar el Gwent_Observation para poder hacer el acto de la observacion
        #obs = GwentObservation(randomized_main_deck, randomized_hands,self.players, self.points_p1,
        #                       self.points_p2, self.turn, self.winner)
        return

    def is_terminal(self):
        return self.lives_p1 == 0 \
               or self.lives_p2 == 0

    def __str__(self):
        s = "PLAYER 1: " + "\n"
        s += "====================" + "\n"
        s += "Lives: " + str(self.lives_p1) + "\n"
        s += "Points: " + str(self.points_p1) + "\n"
        s += "Hand: " + str(self.hands[0]) + "\n"
        s += "Terrain: " + str(self.terrain_p1) + "\n"
        s += "Main Deck: \n"
        for card in self.randomized_main_deck_0.get_cards():
            s += "  " + str(card) + "\n"
        s += "--------------------" + "\n"
        s += "PLAYER 2: " + "\n"
        s += "====================" + "\n"
        s += "Lives: " + str(self.lives_p2) + "\n"
        s += "Points :" + str(self.points_p2) + "\n"
        s += "Hand: " + str(self.hands[1]) + "\n"
        s += "Terrain: " + str(self.terrain_p2) + "\n"
        s += "Main Deck: \n"
        for card in self.randomized_main_deck_1.get_cards():
            s += "  " + str(card) + "\n"
        s += "--------------------" + "\n"
        s += "TURN :" + str(self.turn) + "\n"
        return s
