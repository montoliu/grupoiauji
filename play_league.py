from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer
from main_functions import select_game, play_one_match

# ---------------------------------------------------------------------------
# MAIN: Plays several games among several players
# The winning player of a game gets 1 point
# When there is a Tie, both players get 0.5 points
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    # TODO make these variables arg of the main program
    budget = 1000                      # 1 second
    game_name = "TicTacToe"            # Gwent, ClashRoyale, TicTacToe
    verbose = 0                        # print messages OFF
    n_matches = 1000

    game, game_state, forward_model, heuristic = select_game(game_name)

    # List of players of the league
    l_players = [RandomPlayer(), OSLAPlayer(), AlwaysFirstPlayer()]

    l_points = [0.0 for i in range(len(l_players))]  # 0.0 points for each player
    n_matches = int(n_matches / 2)

    i = 0
    for p1 in l_players:
        j = 0
        for p2 in l_players:
            if p1 != p2:
                # i (p1) vs j (p2)
                for n in range(n_matches):
                    # player i as first
                    game.reset(game_state, 1)
                    play_one_match(game_state, forward_model, heuristic, p1, p2, budget, verbose)
                    if game_state.winner == 1:
                        l_points[i] += 1
                    elif game_state.winner == 2:
                        l_points[j] += 1
                    else:
                        l_points[i] += 0.5    # When there is a Tie, half for each player
                        l_points[j] += 0.5

                    # player i as second
                    game.reset(game_state, 2)
                    play_one_match(game_state, forward_model, heuristic, p1, p2, budget, verbose)
                    if game_state.winner == 1:
                        l_points[i] += 1
                    elif game_state.winner == 2:
                        l_points[j] += 1
                    else:
                        l_points[i] += 0.5
                        l_points[j] += 0.5
            j += 1
        i += 1

    for i in range(len(l_players)):
        print("Player" + str(l_players[i]) + " got " + str(l_points[i]) + " points")
