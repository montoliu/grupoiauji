from Games.ClashRoyale.ClashRoyaleGame import ClashRoyaleGame
from Games.ClashRoyale.ClashRoyaleGameState import ClashRoyaleGameState

if __name__ == '__main__':
    game = ClashRoyaleGame()
    game_state = ClashRoyaleGameState()

    quien_es_el_primero = 0

    game.reset(game_state, quien_es_el_primero)

    print(game_state)

