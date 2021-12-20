from Games.Gwent.GwentGame import GwentGame
from Games.Gwent.GwentGameState import GwentGameState

if __name__ == '__main__':
    game = GwentGame()
    game_state = GwentGameState()

    who_plays_first = 0

    game.reset(game_state, who_plays_first)

    print(game_state)