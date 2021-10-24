import random
from Players.RandomPlayer import RandomPlayer
from Games.TicTacToe.TicTacToeGame import TicTacToeGame
from Games.TicTacToe.TicTacToeGameState import TicTacToeGameState
from Games.TicTacToe.TicTacToeForwardModel import TicTacToeForwardModel
from Games.TicTacToe.TicTacToeHeuristic import TicTacToeHeuristic


# Given the game name, create the game, game_state, forward model and heuristic of this game
def select_game(game_name):
    game = None
    game_state = None
    forward_model = None
    heuristic = None

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
        game = TicTacToeGame()
        game_state = TicTacToeGameState()
        forward_model = TicTacToeForwardModel()
        heuristic = TicTacToeHeuristic()
    return game, game_state, forward_model, heuristic


if __name__ == '__main__':
    # TODO make this two variables arg of the main program
    budget = 1000                      # 1 second
    game_name = "TicTacToe"            # Gwent, ClashRoyale, TicTacToe

    game, game_state, forward_model, heuristic = select_game(game_name)

    player1 = RandomPlayer()
    player2 = RandomPlayer()

    player_id_as_first = random.choice([1, 2])   # 1 or 2
    game.reset(game_state, player_id_as_first)

    while not game_state.is_terminal():
        print("Game State: ")
        print(game_state)
        list_actions = game_state.get_list_actions()
        if game_state.turn == 1:
            action = player1.think(list_actions, budget)
        else:
            action = player2.think(list_actions, budget)
        print("Player " + str(game_state.turn) + " selects " + str(action))
        forward_model.play(game_state, action, heuristic)

        if game_state.is_terminal():
            break

        print(game_state)
        list_actions = game_state.get_list_actions()
        if game_state.turn == 1:
            action = player1.think(list_actions, budget)
        else:
            action = player2.think(list_actions, budget)
        print("Player " + str(game_state.turn) + " selects " + str(action))
        forward_model.play(game_state, action, heuristic)

    print(game_state)
    print("The winner is the player: " + str(game_state.winner))
