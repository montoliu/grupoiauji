from Core.Observation import Observation
from Games.ClashRoyale.ClashRoyaleAction import ClashRoyaleAction


class ClashRoyaleObservation(Observation):
    def __init__(self, gs_turn, gs_hand_p1, gs_hand_p2, gs_elixir_p1, gs_elixir_p2):
        # TODO: completar
        self.turn = gs_turn
        self.hand_p1 = gs_hand_p1       # hay que hacer un deep copy
        self.hand_p2 = gs_hand_p2       # hay que hacer un deep copy
        self.elixir_p1 = gs_elixir_p1
        self.elixir_p2 = gs_elixir_p2

    def get_list_actions(self):
        l_actions = []
        if self.turn == 0:
            for card in self.hand_p1.get_cards():
                if card.cost <= self.elixir_p1:
                    for pos in ["L", "M", "R"]:
                        l_actions.append(ClashRoyaleAction(card, pos))
        else:
            for card in self.hand_p2.get_cards():
                if card.cost <= self.elixir_p2:
                    for pos in ["L", "M", "R"]:
                        l_actions.append(ClashRoyaleAction(card, pos))

        l_actions.append(ClashRoyaleAction(None, None))   # no play action
        return l_actions
