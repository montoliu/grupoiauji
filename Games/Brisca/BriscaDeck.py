import random


class BriscaDeck:
    def __init__(self):
        self.l_cards = []

    def shuffle(self):
        random.shuffle(self.l_cards)

    def draw(self):
        card = self.l_cards[0]
        self.l_cards.pop(0)