from Core.Action import Action


# ---------------------------------------------------------------------------
# An Action is the card to be played on the board
# ---------------------------------------------------------------------------
class GwentAction(Action):
    def __init__(self, card):
        self.card = card

    def get_card(self):
        return self.card

    def __str__(self):
        return str(self.card)
