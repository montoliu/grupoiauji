class ClashRoyaleUnit:
    def __init__(self):
        self.unit_id = None
        self.player_id = None
        self.health = None
        self.name = None
        self.damage = None
        self.speed = None
        self.hit_range = None

    def assign(self, unit_id, player_id, card):
        self.unit_id = unit_id
        self.player_id = player_id
        self.health = card.health
        self.name = card.name
        self.damage = card.damage
        self.speed = card.speed
        self.hit_range = card.hit_range

    def is_empty(self):
        return self.unit_id is None

    def __str__(self):
        return self.name + " [" \
               + str(self.health) + ", " \
               + str(self.damage) + ", " \
               + str(self.speed) + ", " \
               + str(self.hit_range) + "]"

