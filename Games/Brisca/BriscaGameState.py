import random

from Core.GameState import GameState
from Games.Brisca.BriscaCardCollection import BriscaCardCollection
from Games.Brisca.BriscaObservation import BriscaObservation


class BriscaGameState(GameState):
    def __init__(self):
        self.n_players = 4
        self.turn = 0
        self.trump_card = None
        self.played_cards = BriscaCardCollection()
        self.main_deck = BriscaCardCollection()
        self.hands = []
        self.won_cards = []

    # get the observable view for actual player
    # non observable parts are randomized
    def get_observation(self):
        l_all_cards = []
        l_all_cards.extend(self.main_deck.get_cards())
        for p in range(self.n_players):
            if p != self.turn:
                l_all_cards.extend(self.hands[p].get_cards())

        random.shuffle(l_all_cards)

        # draw cards to opponent hand
        randomized_main_deck = BriscaCardCollection()
        randomized_main_deck.add_cards(l_all_cards)
        randomized_hands = []

        n = self.hands[0].len()  # number of card on hand

        for p in range(self.n_players):
            randomized_hands.append(BriscaCardCollection())
            if p != self.turn:
                # draw n cards from randomized main_deck
                for i in range(n):
                    card = randomized_main_deck.draw()
                    randomized_hands[p].add_card(card)
            else:
                # same cards for actual player
                for i in range(n):
                    card = self.hands[p].get_card(i)
                    randomized_hands[p].add_card(card)

        obs = BriscaObservation(randomized_main_deck, randomized_hands, self.trump_card,
                                self.won_cards, self.turn, self.n_players, self.played_cards)
        return obs

    # empty deck, empty hands
    def is_terminal(self):
        return self.main_deck.empty() \
               and self.hands[0].epmty() \
               and self.hands[1].epmty() \
               and self.hands[2].epmty() \
               and self.hands[3]

    def __str__(self):
        s = "DECK:  " + str(self.main_deck) + "\n"
        s += "TURN:  " + str(self.turn) + "\n"
        s += "TRUMP: " + str(self.trump_card) + "\n"
        s += "HANDS: \n"
        for hand in self.hands:
            s += "   " + str(hand) + "\n"
        s += "PLAYED CARDS: " + str(self.played_cards) + "\n"
        s += "WON CARDS: \n"
        for cards in self.won_cards:
            s += "   " + str(cards) + "\n"
        return s
