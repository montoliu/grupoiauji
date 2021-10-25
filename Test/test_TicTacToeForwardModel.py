from unittest import TestCase

from Games.TicTacToe.TicTacToeAction import TicTacToeAction
from Games.TicTacToe.TicTacToeForwardModel import TicTacToeForwardModel
from Games.TicTacToe.TicTacToeGame import TicTacToeGame
from Games.TicTacToe.TicTacToeGameState import TicTacToeGameState
from Games.TicTacToe.TicTacToeHeuristic import TicTacToeHeuristic


class TestTicTacToeForwardModel(TestCase):
    def test_play1(self):
        game = TicTacToeGame()
        fm = TicTacToeForwardModel()
        gs = TicTacToeGameState()
        h = TicTacToeHeuristic()

        game.reset(gs, 1)
        action = TicTacToeAction(0, 0)    # player 1 plays [0, 0]
        fm.play(gs, action, h)

        expected = 1
        actual = gs.board[0][0]
        self.assertEqual(expected, actual)

    def test_play2(self):
        game = TicTacToeGame()
        fm = TicTacToeForwardModel()
        gs = TicTacToeGameState()
        h = TicTacToeHeuristic()

        game.reset(gs, 2)
        action = TicTacToeAction(1, 1)  # player 2 plays [0, 0]
        fm.play(gs, action, h)

        expected = 2
        actual = gs.board[1][1]
        self.assertEqual(expected, actual)
