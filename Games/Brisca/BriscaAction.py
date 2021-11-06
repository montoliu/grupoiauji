from Core.Action import Action


class BriscaAction(Action):
    def __init__(self, card):
        self.card = card

    def get_action_type(self):
        return "PLAY_CARD"

    def get_card(self):
        return self.card
