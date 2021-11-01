from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer
from Games.TicTacToe.TicTacToeGame import TicTacToeGame
from Games.TicTacToe.TicTacToeGameState import TicTacToeGameState
from Games.TicTacToe.TicTacToeForwardModel import TicTacToeForwardModel
from Games.TicTacToe.TicTacToeHeuristic import TicTacToeHeuristic


# Given the game name, create the game, game_state, forward model and heuristic of this game
def select_game(game_name):
    gm = None
    gs = None
    fm = None
    ht = None

    # if game_name == "Gwent":
    #     game = GwentGame()
    #     game_state = GwentGameState()
    #     forward_model = GwentForwardModel()
    #     heuristic = GwentHeuristic()
    # elif game_name == "ClashRoyale":
    #     game = ClashRoyaleGame()
    #     game_state = ClashRoyaleGameState()
    #     forward_model = ClashRoyaleForwardModel()
    #     heuristic = ClashRoyaleHeuristic()

    if game_name == "TicTacToe":
        gm = TicTacToeGame()
        gs = TicTacToeGameState()
        fm = TicTacToeForwardModel()
        ht = TicTacToeHeuristic()
    return gm, gs, fm, ht


def player_turn(gs, fm, ht, pl, budget, vbose):
    if vbose:
        print(gs)

    observation = gs.get_observation()
    action = pl.think(observation, budget)

    if vbose:
        print("Player " + str(gs.turn) + " selects [" + str(action) + "]")

    reward = fm.play(gs, action, ht)

    if vbose:
        print("Reward: " + str(reward))


def play_one_match(gs, fm, ht, p1, p2, budget, vbose):
    while not gs.is_terminal():
        if gs.turn == 1:
            player_turn(gs, fm, ht, p1, budget, vbose)
        else:
            player_turn(gs, fm, ht, p2, budget, vbose)

        if gs.is_terminal():
            break

        if gs.turn == 1:
            player_turn(gs, fm, ht, p1, budget, vbose)
        else:
            player_turn(gs, fm, ht, p2, budget, vbose)
