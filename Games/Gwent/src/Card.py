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

carta1 = MeleeCard("ogro", 69, "Es feo")
carta2 = RangedCard("sniper", 69, "Es sniper")
carta3 = ArtilleryCard("catapulta", 69, "Esta guapa")

print(carta1.card_type)
print(carta2.card_type)
print(carta3.card_type)
