import random

from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.HumanPlayer import HumanPlayer
from main_functions import play_one_match, select_game
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer


# ---------------------------------------------------------------------------
# MAIN: Play just one game between two players
# When the match ends, game_state.winner has the player id of the winner or 0 if there is a tie
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 1000                      # 1 second
    game_name = "Brisca"            # Gwent, ClashRoyale, TicTacToe, Brisca
    verbose = 1                        # print messages
    seed = 1
    random.seed(seed)

    game, game_state, forward_model, heuristic = select_game(game_name)

    # RandomPlayer, OSLAPlayer, HumanPlayer
    l_players = [AlwaysFirstPlayer(), AlwaysFirstPlayer(), AlwaysFirstPlayer(), AlwaysFirstPlayer()]

    # who starts? Randomly selected
    player_id_as_first = random.choice(range(game_state.n_players))
    game.reset(game_state, player_id_as_first)

    play_one_match(game_state, forward_model, heuristic, l_players, budget, verbose)

    if verbose:
        print("---------------------------------------- ")
        print("The winner is the player: " + str(l_players[game_state.winner]))
        print(game_state)
