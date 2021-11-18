from Players.AlwaysFirstPlayer import AlwaysFirstPlayer
from Players.OSLAPlayer import OSLAPlayer
from Players.RandomPlayer import RandomPlayer
from main_functions import select_game, play_one_match


def actualize_points(l_pts, winner, ith, jth):
    if winner == 0:
        l_pts[ith] += 1
    elif winner == 1:
        l_pts[jth] += 1
    else:
        l_pts[ith] += 0.5  # When there is a Tie, half for each player
        l_pts[jth] += 0.5


# ---------------------------------------------------------------------------
# MAIN: Plays several games among several players
# The winning player of a game gets 1 point
# When there is a Tie, both players get 0.5 points
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    budget = 2                      # In second
    game_name = "Brisca"         # Gwent, ClashRoyale, TicTacToe
    verbose = False                 # print messages OFF
    n_matches = 100
    controlling_time = False

    game, game_state, forward_model, heuristic = select_game(game_name)

    # List of players of the league
    l_players = [AlwaysFirstPlayer(), RandomPlayer()]

    l_points = [0.0 for i in range(len(l_players))]  # 0.0 points for each player
    n_matches = int(n_matches / 2)

    for i in range(len(l_players)):
        p1 = l_players[i]
        for j in range(i+1, len(l_players)):
            p2 = l_players[j]
            if game_name == "Brisca":
                players = [p1, p2, p1, p2]
            else:
                players = [p1, p2]
            for n in range(n_matches):
                # player i as first
                game.reset(game_state, 0)
                play_one_match(game_state, forward_model, heuristic, players, budget, verbose, controlling_time)
                actualize_points(l_points, game_state.winner, i, j)

                # player j as first
                game.reset(game_state, 1)
                play_one_match(game_state, forward_model, heuristic, players, budget, verbose,controlling_time)
                actualize_points(l_points, game_state.winner, i, j)

    for i in range(len(l_players)):
        print("Player" + str(l_players[i]) + " got " + str(l_points[i]) + " points")


