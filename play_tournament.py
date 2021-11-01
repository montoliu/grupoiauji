from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer
from main_functions import play_one_match, select_game

# ---------------------------------------------------------------------------
# MAIN: plays several games between two players
# Half of the matches the player id 1 plays as first, half as second
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 1000                      # 1 second
    game_name = "TicTacToe"            # Gwent, ClashRoyale, TicTacToe
    verbose = 0                        # print messages OFF
    n_matches = 1000

    game, game_state, forward_model, heuristic = select_game(game_name)

    # Players
    player1 = RandomPlayer()
    player2 = OSLAPlayer()

    player1_wins = 0
    player2_wins = 0
    ties = 0

    n_matches = int(n_matches / 2)
    for n in range(n_matches):
        # player 1 as first
        game.reset(game_state, 1)
        play_one_match(game_state, forward_model, heuristic, player1, player2, budget, verbose)
        if game_state.winner == 1:
            player1_wins += 1
        elif game_state.winner == 2:
            player2_wins += 1
        else:
            ties += 1

        # player 2 as first
        game.reset(game_state, 2)
        play_one_match(game_state, forward_model, heuristic, player1, player2, budget, verbose)
        if game_state.winner == 1:
            player1_wins += 1
        elif game_state.winner == 2:
            player2_wins += 1
        else:
            ties += 1

    print("Player " + str(player1) + " wins: " + str(player1_wins))
    print("Player " + str(player2) + " wins: " + str(player2_wins))
    print("Ties: " + str(ties))
