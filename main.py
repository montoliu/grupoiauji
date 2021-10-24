from Players.RandomPlayer import RandomPlayer


# Given the game name, create the game, game_state, forward model and heuristic of this game
def select_game(game_name):
    game = None
    game_state = None
    forward_model = None
    heuristic = None

    if game_name == "Gwent":
        game = GwentGame()
        game_state = GwentGameState()
        forward_model = GwentForwardModel()
        heuristic = GwentHeuristic()
    elif game_name == "ClashRoyale":
        game = ClashRoyaleGame()
        game_state = ClashRoyaleGameState()
        forward_model = ClashRoyaleForwardModel()
        heuristic = ClashRoyaleHeuristic()

    return game, game_state, forward_model, heuristic


if __name__ == '__main__':
    # TODO make this two variables arg of the main program
    budget = 1000                      # 1 second
    game_name = "Gwent"                # Gwent or ClashRoyale

    game, game_state, forward_model, heuristic = select_game(game_name)

    player1 = RandomPlayer()
    player2 = RandomPlayer()

    game.initializate(game_state)

    while not game_state.there_is_a_winner():
        list_actions = game_state.get_list_actions()
        action = player1.think(list_actions, budget)
        forward_model(game_state, action)

        if game_state.there_is_a_winner():
            break

        list_actions = game_state.get_list_actions()
        action = player2.think(list_actions, budget)
        forward_model(game_state, action)

    print("The winner is the player: " + game_state.get_winner())
