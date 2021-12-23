class ClashRoyaleUnit:
    def __init__(self, card):
        self.health = card.health
        self.name = card.name
        self.damage = card.damage
        self.speed = card.speed
        self.hit_range = card.hit_range

    def __str__(self):
        return "UNIT"
