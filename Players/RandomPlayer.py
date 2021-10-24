import random


class RandomPlayer:
    def think(self, list_actions, budget):
        return random.choice(list_actions)
