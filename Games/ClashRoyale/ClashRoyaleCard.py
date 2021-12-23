class ClashRoyaleCard:
    def __init__(self):
        self.name = "Troop"
        self.damage = 50
        self.health = 500
        self.speed = 1
        self.hit_range = 1
        self.cost = 3

    def __str__(self):
        s = self.name \
            + " [" + str(self.damage) \
            + ", " + str(self.health) \
            + ", " + str(self.speed) \
            + ", " + str(self.hit_range) \
            + ", " + str(self.cost) \
            + "]"
        return s


#class TroopCard(Card):
    #def __init__(self, card_name, level, cost, damage, hitpoints, hit_speed, speed, hit_range):
        #super().__init__(self, card_name)
        #self.damage = damage
        #self.hitpoints = hitpoints
        #self.hit_speed = hit_speed
        #self.speed = speed
        #self.hit_range = hit_range

#class SpellCard(Card):
    #def __init__(self, card_name, level, cost, radius):
        #super().__init__(self, card_name)
        #self.radius = radius

#class BuildingCard(Card):
    #def __init__(self, card_name, level, cost, life_time, hit_points):
        #super().__init__(self, card_name)
        #self.life_time = life_time
        #self.hit_points = hit_points
