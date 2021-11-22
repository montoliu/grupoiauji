from unittest import TestCase

from Games.Brisca.BriscaGame import BriscaGame
from Games.Brisca.BriscaGameState import BriscaGameState


class TestBriscaGame(TestCase):
    def test_reset(self):
        gs = BriscaGameState()
        bg = BriscaGame()
        bg.reset(gs, 0)

        # Cards on main deck after drawing
        expected = 28
        actual = gs.main_deck.len()
        self.assertEqual(expected, actual)

        # Cards on players hand after drawing
        expected = 3
        actual = gs.hands[0].len()
        self.assertEqual(expected, actual)

        expected = 3
        actual = gs.hands[1].len()
        self.assertEqual(expected, actual)

        expected = 3
        actual = gs.hands[2].len()
        self.assertEqual(expected, actual)

        expected = 3
        actual = gs.hands[3].len()
        self.assertEqual(expected, actual)

        # Cards on players won set after drawing
        expected = 0
        actual = gs.won_cards[0].len()
        self.assertEqual(expected, actual)

        expected = 0
        actual = gs.won_cards[1].len()
        self.assertEqual(expected, actual)

        expected = 0
        actual = gs.won_cards[2].len()
        self.assertEqual(expected, actual)

        expected = 0
        actual = gs.won_cards[3].len()
        self.assertEqual(expected, actual)

        # The last card of the main deck and the trump onr are the same
        expected = gs.trump_card
        actual = gs.main_deck.l_cards[len(gs.main_deck.l_cards)-1]
        self.assertEqual(expected, actual)
