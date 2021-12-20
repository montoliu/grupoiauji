from Core.Observation import Observation
from Games.ClashRoyale.ClashRoyaleAction import ClashRoyaleAction


class ClashRoyaleObservation(Observation):
    def __init__(self, gs_deck_p1, gs_elixir_p1, gs_winner, gs_towers_p1,
                 gs_towers_p2, gs_hand_p1, gs_units_p1, gs_units_p2, gs_time):
        self.winner = gs_winner
        self.deck_p1 = gs_deck_p1
        self.elixir_p1 = gs_elixir_p1
        self.towers_p1 = gs_towers_p1
        self.towers_p2 = gs_towers_p2
        self.hand_p1 = gs_hand_p1
        self.units_p1 = gs_units_p1
        self.units_p2 = gs_units_p2
        self.time = gs_time
        self.n_players = 2

    def get_list_actions(self):
        l_actions = []
        for card in self.hand_p1:
            # Suponiendo que card tiene un atributo cost
            if card.cost <= self.elixir_p1:
                l_actions.append(ClashRoyaleAction(card, card_pos))

# no jugar y por cada carta, tres posiciones
        return l_actions