import random
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


def player_turn(gs, fm, ht, pl, vbose):
    if vbose:
        print(gs)

    list_actions = gs.get_list_actions()
    action = pl.think(list_actions, budget)

    if vbose:
        print("Player " + str(gs.turn) + " selects [" + str(action) + "]")

    reward = fm.play(game_state, action, ht)

    if vbose:
        print("Reward: " + str(reward))


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # TODO make these variables arg of the main program
    budget = 1000                      # 1 second
    game_name = "TicTacToe"            # Gwent, ClashRoyale, TicTacToe
    verbose = 1                        # print messages

    game, game_state, forward_model, heuristic = select_game(game_name)

    player1 = RandomPlayer()
    player2 = RandomPlayer()

    player_id_as_first = random.choice([1, 2])   # 1 or 2
    game.reset(game_state, player_id_as_first)

    while not game_state.is_terminal():
        if game_state.turn == 1:
            player_turn(game_state, forward_model, heuristic, player1, verbose)
        else:
            player_turn(game_state, forward_model, heuristic, player2, verbose)

        if game_state.is_terminal():
            break

        if game_state.turn == 1:
            player_turn(game_state, forward_model, heuristic, player1, verbose)
        else:
            player_turn(game_state, forward_model, heuristic, player2, verbose)

    if verbose:
        print(game_state)
        print("The winner is the player: " + str(game_state.winner))
