import random

from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.HumanPlayer import HumanPlayer
from Players.SlowPlayer import SlowPlayer
from main_functions import play_one_match, select_game
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer


# ---------------------------------------------------------------------------
# MAIN: Play just one game between two players
# When the match ends, game_state.winner has the player id of the winner or 0 if there is a tie
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 2                      # Time to think for AI in second
    game_name = "Brisca"            # Gwent, ClashRoyale, TicTacToe, Brisca
    verbose = True                  # print messages ON/OFF
    controlling_time = True        # If the player time to think is going to be controlled ON/OFF

    #seed = 1                        # random seed
    #random.seed(seed)

    game, game_state, forward_model, heuristic = select_game(game_name)
    player_id_as_first = random.choice(range(game_state.n_players))
    game.reset(game_state, player_id_as_first)

    l_players = [RandomPlayer(), AlwaysFirstPlayer()]

    if game_name == "Brisca":
        l_players.append(l_players[0])
        l_players.append(l_players[1])

    play_one_match(game_state, forward_model, heuristic, l_players, budget, verbose, controlling_time)

    if verbose:
        print("")
        print("*** ------------------------------------------------- ")
        if game_state.winner != -1:
            print("*** The winner is the player: " + str(game_state.winner) + " " + str(l_players[game_state.winner]))
        else:
            print("*** The is a Tie.")
        print("*** ------------------------------------------------- ")

