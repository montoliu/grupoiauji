class ClashRoyaleCell:
    def __init__(self):
        self.unit_id = None
        self.player_id = None

    def is_empty(self):
        return self.unit_id is None

    def __str__(self):
        s = ""
        if not self.is_empty():
            s += str(self.unit_id)
        return s
