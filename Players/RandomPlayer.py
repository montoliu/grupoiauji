import random

from Core.Player import Player


# ---------------------------------------------------------------------------
# Randomly selects one action from the list of possible actions
# ---------------------------------------------------------------------------
class RandomPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        return random.choice(list_actions)

    def __str__(self):
        return "RandomPlayer"
