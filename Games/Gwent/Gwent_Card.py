class Card:
    def __init__(self, card_name, level, effect):
        self.card_name = card_name
        self.level = level
        self.effect = effect

class MeleeCard(Card):
    def __init__(self, card_name, level, effect, card_type = "Melee"):
        super().__init__(card_name, level, effect)
        self.card_type = card_type

class RangedCard(Card):
    def __init__(self, card_name, level, effect, card_type = "Ranged"):
        super().__init__(card_name, level, effect)
        self.card_type = card_type

class ArtilleryCard(Card):
    def __init__(self, card_name, level, effect, card_type = "Artillery"):
        super().__init__(card_name, level, effect)
        self.card_type = card_type
