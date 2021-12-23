from Core.Heuristic import Heuristic


class ClashRoyaleHeuristic(Heuristic):
    def get_score(self, observation, player_id):
        # Devuelve como de bueno es estar en el estado mostrado por observation
        # Pensar en la formula
        # TODO, de momento he puesto que siempre devuelve 1
        return 1
    