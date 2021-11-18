import time
from Core.Player import Player


# ---------------------------------------------------------------------------
# Wait a long time period (more than budget allowed) and then returns the first action
# ---------------------------------------------------------------------------
class SlowPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        time.sleep(2*budget)
        return list_actions[0]

    def __str__(self):
        return "SlowPlayer"
