from unittest import TestCase

from Games.Gwent import GwentGame
from Games.Gwent.GwentGameState import GwentGameState


class TestGwentGame(TestCase):
    def test_reset(self):
        gs = GwentGameState()
        bg = GwentGame()
        bg.reset(gs, 0)

        # Cards on deck p1 after drawing
        expected = 5
        actual = gs.main_deck.len()
        self.assertEqual(expected, actual)

        # Cards on deck p2 after drawing
        expected = 5
        actual = gs.main_deck.len()
        self.assertEqual(expected, actual)

        # Cards on players hand after drawing
        expected = 4
        actual = gs.hands[0].len()
        self.assertEqual(expected, actual)

        expected = 4
        actual = gs.hands[1].len()
        self.assertEqual(expected, actual)

        # Cards on player 1 terrain at the start
        expected = 0
        actual = gs.terrain_p1.len()
        self.assertEqual(expected, actual)

        # Cards on player 2 terrain at the start
        expected = 0
        actual = gs.terrain_p2.len()
        self.assertEqual(expected, actual)

        # Check lives at the start
        expected = 3
        actual = gs.lives_p1
        self.assertEqual(expected, actual)

        expected = 3
        actual = gs.lives_p2
        self.assertEqual(expected, actual)

        # Check points at the start
        expected = 0
        actual = gs.points_p1
        self.assertEqual(expected, actual)

        expected = 0
        actual = gs.points_p2
        self.assertEqual(expected, actual)



