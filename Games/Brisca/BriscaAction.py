from Core.Action import Action


class BriscaAction(Action):
    def __init__(self, card):
        self.card = card

    def get_card(self):
        return self.card
