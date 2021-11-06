from unittest import TestCase

from Games.Brisca.BriscaGame import BriscaGame
from Games.Brisca.BriscaGameState import BriscaGameState


class TestBriscaGameState(TestCase):
    def test_get_observation(self):
        bg = BriscaGame()
        gs = BriscaGameState()
        bg.reset(gs, 0)

        obs = gs.get_observation()
        self.fail()
