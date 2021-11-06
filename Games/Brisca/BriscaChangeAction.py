from Core.Action import Action


class BriscaChangeAction(Action):
    def __init__(self, card_to_change, card_to_play):
        self.card_to_change = card_to_change
        self.card_to_play = card_to_play

    def get_action_type(self):
        return "CHANGE_CARD"

    def get_card_to_change(self):
        return self.card_to_change

    def get_card_to_play(self):
        return self.card_to_play
