import random

import func_timeout
from Games.Brisca.BriscaForwardModel import BriscaForwardModel
from Games.Brisca.BriscaGame import BriscaGame
from Games.Brisca.BriscaGameState import BriscaGameState
from Games.Brisca.BriscaHeuristic import BriscaHeuristic
from Games.TicTacToe.TicTacToeGame import TicTacToeGame
from Games.TicTacToe.TicTacToeGameState import TicTacToeGameState
from Games.TicTacToe.TicTacToeForwardModel import TicTacToeForwardModel
from Games.TicTacToe.TicTacToeHeuristic import TicTacToeHeuristic


# ---------------------------------------------------------------------------
# Given the game name, create the game, game_state, forward model and heuristic of this game
# ---------------------------------------------------------------------------
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
    elif game_name == "Brisca":
        gm = BriscaGame()
        gs = BriscaGameState()
        fm = BriscaForwardModel()
        ht = BriscaHeuristic()
    return gm, gs, fm, ht


# ---------------------------------------------------------------------------
# Performs a player turn
# ---------------------------------------------------------------------------
def player_turn(gs, fm, ht, pl, budget, verbose, controlling_time):
    if verbose:
        print("")
        print("---------------------------------------- ")
        print("Player " + str(gs.turn) + " [" + str(pl) + "] turn")
        print("---------------------------------------- ")
        print(str(gs))

    observation = gs.get_observation()
    if controlling_time:
        try:
            action = func_timeout.func_timeout(budget, player_thinking, args=[pl, observation, budget])
        except func_timeout.FunctionTimedOut:
            if verbose:
                print("Ups, too many time thinking. A random action is selected instead !!!")
            action = get_random_action(observation)
    else:
        action = player_thinking(pl, observation, budget)

    if verbose:
        print("Player " + str(gs.turn) + " selects [" + str(action) + "]")

    reward = fm.play(gs, action, ht)

    if verbose:
        print("Reward: " + str(reward))


def player_thinking(pl, observation, budget):
    return pl.think(observation, budget)


def get_random_action(observation):

    l_actions = observation.get_list_actions()
    return random.choice(l_actions)


# ---------------------------------------------------------------------------
# Plays just one match
# ---------------------------------------------------------------------------
def play_one_match(gs, fm, ht, l_players, budget, verbose, controlling_time):
    while not gs.is_terminal():
        for i in range(gs.n_players):
            player_turn(gs, fm, ht, l_players[gs.turn], budget, verbose, controlling_time)
            if gs.is_terminal():
                break

    fm.check_winner(gs)
