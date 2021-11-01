import random
from functions import play_one_match, select_game
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer


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
    player2 = OSLAPlayer()

    player_id_as_first = random.choice([1, 2])   # 1 or 2
    game.reset(game_state, player_id_as_first)

    play_one_match(game_state, forward_model, heuristic, player1, player2, budget, verbose)

    if verbose:
        print(game_state)
        print("The winner is the player: " + str(game_state.winner))
