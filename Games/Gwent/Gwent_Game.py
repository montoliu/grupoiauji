from Core.Game import Game
from Games.Gwent.Gwent_Card import Gwent_Card
from Games.Gwent.Gwent_Card_Collection import GwentCardCollection

class GwentGame(Game):

    # initialize game state
    def reset(self, game_state, player_id_as_first):
        self.create_deck_player_1(game_state.deck_player_1)
        self.create_deck_player_2(game_state.deck_player_2)

        # create empty hands
        for i in range(game_state.players):
            hand = GwentCardCollection()
            game_state.hands.append(hand)

        # draw three cards to player 1
        for j in range(3):
            card = game_state.deck_player_1.draw()
            game_state.hands.append(hand)

        # draw three cards to player 2
        for k in range(3):
            card = game_state.deck_player_2.draw()
            game_state.hands.append(hand)

        # reset board
        game_state.terrain_p1.clear()
        game_state.terrain_p2.clear()

        # reset lives nad points
        game_state.lives_p1 = 3
        game_state.lives_p2 = 3
        game_state.points_p1 = 0
        game_state.points_p2 = 0

        # who play as first
        game_state.turn = player_id_as_first