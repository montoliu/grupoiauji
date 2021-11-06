from Core.Observation import Observation
from Games.Brisca.BriscaAction import BriscaAction
from Games.Brisca.BriscaChangeAction import BriscaChangeAction


class BriscaObservation(Observation):
    def __init__(self, main_deck, hands, trump_card, won_cards, turn, n_players, played_cards):
        self.main_deck = main_deck.clone()
        self.hands = self.clone_list(hands)
        self.trump_card = trump_card
        self.won_cards = self.clone_list(won_cards)
        self.turn = turn
        self.n_players = n_players
        self.played_cards = played_cards.clone()

    def get_list_actions(self):
        l_actions = []
        for card in self.hands[self.turn]:
            l_actions.append(BriscaAction(card))

        # if the player has the 7th of the same type than the trump card
        # or the player has the 2th of the same type than the trump card and this the 7th
        for card in self.hands[self.turn]:
            if card.get_number() == 7 and card.get_type() == self.trump_card.get_type():
                for card_to_play in self.hands[self.turn]:
                    l_actions.append(BriscaChangeAction(card, card_to_play))
                break
            elif card.get_number() == 2 and \
                    card.get_type() == self.trump_card.get_type() and self.trump_card.get_number == 2:
                for card_to_play in self.hands[self.turn]:
                    l_actions.append(BriscaChangeAction(card, card_to_play))
                break

        return l_actions

    def clone(self):
        new_main_deck = self.main_deck.clone()
        new_hands = self.clone_list(self.hands)
        new_trump_card = self.trump_card
        new_won_cards = self.clone_list(self.won_cards)
        new_turn = self.turn
        new_n_players = self.n_players
        new_played_cards = self.played_cards.clone()
        new_obs = BriscaObservation(new_main_deck, new_hands, new_trump_card,
                                    new_won_cards, new_turn, new_n_players, new_played_cards)
        return new_obs

    def clone_list(self, old_list):
        new_list = []
        for element in old_list:
            new_list.append(element.clone())
        return new_list
