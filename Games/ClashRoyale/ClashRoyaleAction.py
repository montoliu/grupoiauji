from Core.Action import Action


class ClashRoyaleAction(Action):
    def __init__(self, card, card_pos):
        self.card = card
        self.card_pos = card_pos

    def __str__(self):
        if self.card is None:
            s = "No action"
        else:
            s = "{" + str(self.card) + ", " + str(self.card_pos) + "}"
        return s
