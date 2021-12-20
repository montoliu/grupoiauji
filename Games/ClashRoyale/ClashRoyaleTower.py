
class ClashRoyaleTower:
    def __init__(self):
        self.vida = 1000
        self.range = 7
        self.damage = 50

    def decrease_life(self, amount):
        self.vida -= amount

    def reset(self):
        self.vida = 1000
