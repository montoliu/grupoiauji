from Core.Action import Action


class ClashRoyaleAction(Action):
    def __init__(self, card, position):
        self.card = card
        self.position = position

    def is_noaction(self):
        return self.card is None

    def __str__(self):
        if self.card is None:
            s = "No action"
        else:
            s = "{" + str(self.card) + ", " + str(self.position) + "}"
        return s
