class BriscaCard:
    def __init__(self, card_type, card_number):
        self.card_type = card_type      # "O", "E", "C", "B"
        self.card_number = card_number  # 1 to 7 and 10 to 12 (no 8 and 9)

    def get_points(self):
        if self.card_number == 1:
            return 11
        if self.card_number == 3:
            return 10
        if self.card_number == 12:
            return 4
        if self.card_number == 11:
            return 3
        if self.card_number == 10:
            return 2
        return 0
