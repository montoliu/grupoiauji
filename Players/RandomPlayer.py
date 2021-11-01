import random

from Core.Player import Player


class RandomPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        return random.choice(list_actions)

    def __str__(self):
        return "RandomPlayer"
