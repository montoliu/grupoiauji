from Games.ClashRoyale.ClashRoyaleForwardModel import ClashRoyaleForwardModel
from Games.ClashRoyale.ClashRoyaleGame import ClashRoyaleGame
from Games.ClashRoyale.ClashRoyaleGameState import ClashRoyaleGameState
from Games.ClashRoyale.ClashRoyaleHeuristic import ClashRoyaleHeuristic

if __name__ == '__main__':
    game = ClashRoyaleGame()
    game_state = ClashRoyaleGameState()
    forward_model = ClashRoyaleForwardModel()
    heuristic = ClashRoyaleHeuristic()

    player_id_as_first = 0

    game.reset(game_state, player_id_as_first)

    print(game_state)

    obs = game_state.get_observation()
    l_actions = obs.get_list_actions()

    print("Actions: ")
    for a in l_actions:
        print(a)

    # Simular que se toma una action (e.g. la primera) y ejecutar play en el FM
    forward_model.play(game_state, l_actions[0], heuristic)

    print(game_state)