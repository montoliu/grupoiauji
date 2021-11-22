from Core.GameState import GameState


class GwentGameState(GameState):

    def __init__(self, lives_p1, lives_p2, points_p1, points_p2, hand_p1, hand_p2, terrain_p1, terrain_p2, turn):
        self.lives_p1 = lives_p1
        self.lives_p2 = lives_p2
        self.points_p1 = points_p1
        self.points_p2 = points_p2
        self.hand_p1 = hand_p1
        self.hand_p2 = hand_p2
        self.terrain_p1 = terrain_p1
        self.terrain_p2 = terrain_p2
        self.turn = turn

    def __str__(self):
        return str(self.lives_p1) + ", " + self.lives_p2 + ", " + self.points_p1 + ", " + self.points_p2 \
               + ", " + self.hand_p1 + ", " + self.hand_p2 + ", " + self.terrain_p1 + ", " + self.terrain_p2 + ", " + self.turn + "."
