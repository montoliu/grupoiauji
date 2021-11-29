class GwentCard:
    def __init__(self, card_name, level, effect):
        self.card_name = card_name
        self.level = level
        self.effect = effect

    def get_type(self):
        return self.card_type

    def get_level(self):
        return self.level

    def get_effect(self):
        return self.effect

    def clone(self):
        new_card = GwentCard(self.card_name, self.level, self.effect, self.card_type)
        return new_card

    def __str__(self):
        return self.card_type + str(self.level)

    def __eq__(self,other):
        return self.card_type == other.card_type and self.level == other.level

class Gwent_Melee_Card(GwentCard):
    def __init__(self, card_name, level, effect, card_type = "Melee"):
        super().__init__(card_name, level, effect)
        self.card_type = card_type

class Gwent_Ranged_Card(GwentCard):
    def __init__(self, card_name, level, effect, card_type = "Ranged"):
        super().__init__(card_name, level, effect)
        self.card_type = card_type

class Gwent_Artillery_Card(GwentCard):
    def __init__(self, card_name, level, effect, card_type = "Artillery"):
        super().__init__(card_name, level, effect)
        self.card_type = card_type
