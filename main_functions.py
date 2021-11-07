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
def player_turn(gs, fm, ht, pl, budget, vbose):
    if vbose:
        print("---------------------------------------- ")
        print("Player " + str(gs.turn) + " [" + str(pl) + "] turn:")
        print("---------------------------------------- ")
        print(gs)

    observation = gs.get_observation()
    action = pl.think(observation, budget)

    if vbose:
        print("Player " + str(gs.turn) + " selects [" + str(action) + "]")

    reward = fm.play(gs, action, ht)

    if vbose:
        print("Reward: " + str(reward))


# ---------------------------------------------------------------------------
# Plays just one match
# ---------------------------------------------------------------------------
def play_one_match(gs, fm, ht, l_players, budget, vbose):
    while not gs.is_terminal():
        for i in range(gs.n_players):
            player_turn(gs, fm, ht, l_players[gs.turn], budget, vbose)
            if gs.is_terminal():
                break
