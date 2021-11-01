import math
import random
from Core.Player import Player
from Games.TicTacToe.TicTacToeForwardModel import TicTacToeForwardModel
from Games.TicTacToe.TicTacToeHeuristic import TicTacToeHeuristic


# For each action calculates how good or bad is to play such us action
# Return the action with the best score, according to the heuristic
# If there are more than one with the best score, returns one of best randomly choosen
class OSLAPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        l_best_action = []
        best_score = -math.inf
        fm = TicTacToeForwardModel()
        ht = TicTacToeHeuristic()

        for action in list_actions:
            obs = observation.clone()
            score = fm.play(obs, action, ht)

            if score > best_score:
                best_score = score
                l_best_action = [action]
            elif score == best_score:
                l_best_action.append(action)

        return random.choice(l_best_action)

    def __str__(self):
        return "OLSAPlayer"
