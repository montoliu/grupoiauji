class Card:
    def __init__(self, card_name, level, cost):
        self.card_name = card_name
        self.level = level
        self.cost = cost

class TroopCard(Card):
    def __init__(self, card_name, level, cost, damage, hitpoints, hit_speed, speed, hit_range):
        super().__init__(self, card_name, level, cost)
        self.damage = damage
        self.hitpoints = hitpoints
        self.hit_speed = hit_speed
        self.speed = speed
        self.hit_range = hit_range

class SpellCard(Card):
    def __init__(self, card_name, level, cost, radius):
        super().__init__(self, card_name, level, cost)
        self.radius = radius

class BuildingCard(Card):
    def __init__(self, card_name, level, cost, life_time, hit_points):
        super().__init__(self, card_name, level, cost)
        self.life_time = life_time
        self.hit_points = hit_points
