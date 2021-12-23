from Core.Observation import Observation
from Games.ClashRoyale.ClashRoyaleAction import ClashRoyaleAction


class ClashRoyaleObservation(Observation):
    def __init__(self, gs_turn, gs_hands,gs_elixir):
        # TODO: completar
        self.turn = gs_turn
        self.hands = gs_hands      # TODO: hay que hacer un deep copy
        self.elixir = gs_elixir    # TODO: hay que hacer un deep copy

    def get_list_actions(self):
        l_actions = []
        for card in self.hands[self.turn].get_cards():
            if card.cost <= self.elixir[self.turn]:
                for pos in ["L", "M", "R"]:
                    l_actions.append(ClashRoyaleAction(card, pos))

        l_actions.append(ClashRoyaleAction(None, None))   # no play action
        return l_actions
