
class ClashRoyaleTower:
    def __init__(self):
        self.health = 1000
        self.range = 7
        self.damage = 50

    def decrease_health(self, amount):
        self.health -= amount

    def reset(self):
        self.health = 1000

    def __str__(self):
        s = "[" + str(self.health) \
            + ", " + str(self.range) \
            + ", " + str(self.damage) \
            + "]"
        return s
