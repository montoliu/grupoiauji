from unittest import TestCase

from Games.Brisca.BriscaCard import BriscaCard
from Games.Brisca.BriscaForwardModel import BriscaForwardModel


class TestBriscaForwardModel(TestCase):
    def actual_situation(self):
        self.fm = BriscaForwardModel()
        self.trump_card = BriscaCard("O", 5)
        self.round_card = BriscaCard("E", 4)

    # Both trump, actual better
    def test_is_better_card_case1(self):
        self.actual_situation()
        actual_card = BriscaCard("O", 3)
        prev_card = BriscaCard("O", 7)
        expected = True
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # Both trump, actual worse
    def test_is_better_card_case2(self):
        self.actual_situation()
        actual_card = BriscaCard("O", 10)
        prev_card = BriscaCard("O", 1)
        expected = False
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # actual trump, prev round
    def test_is_better_card_case3(self):
        self.actual_situation()
        actual_card = BriscaCard("O", 2)
        prev_card = BriscaCard("E", 1)
        expected = True
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # actual round, prev trump
    def test_is_better_card_case4(self):
        self.actual_situation()
        actual_card = BriscaCard("E", 1)
        prev_card = BriscaCard("O", 2)
        expected = False
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # both round, actual best
    def test_is_better_card_case5(self):
        self.actual_situation()
        actual_card = BriscaCard("E", 1)
        prev_card = BriscaCard("E", 7)
        expected = True
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # both round, actual worse
    def test_is_better_card_case6(self):
        self.actual_situation()
        actual_card = BriscaCard("E", 10)
        prev_card = BriscaCard("E", 12)
        expected = False
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # actual round, prev other
    def test_is_better_card_case7(self):
        self.actual_situation()
        actual_card = BriscaCard("E", 2)
        prev_card = BriscaCard("C", 12)
        expected = True
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # actual other, prev round
    def test_is_better_card_case8(self):
        self.actual_situation()
        actual_card = BriscaCard("C", 10)
        prev_card = BriscaCard("E", 2)
        expected = False
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # both other, actual best
    def test_is_better_card_case9(self):
        self.actual_situation()
        actual_card = BriscaCard("C", 10)
        prev_card = BriscaCard("C", 6)
        expected = True
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)

    # both other, actual worse
    def test_is_better_card_case10(self):
        self.actual_situation()
        actual_card = BriscaCard("C", 10)
        prev_card = BriscaCard("C", 12)
        expected = False
        actual = self.fm.is_better_card(actual_card, prev_card, self.trump_card, self.round_card)
        self.assertEqual(expected, actual)