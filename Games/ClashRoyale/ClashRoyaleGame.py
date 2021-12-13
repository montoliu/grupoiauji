from Core.Game import Game
from Games.ClashRoyale.ClahsRoyaleCardCollection import ClashRoyaleCardCollection


class ClashRoyaleGame(Game):
    def reset(self, game_state, player_id_as_first):
        game_state.deck_p1 = ClashRoyaleCardCollection()
        game_state.deck_p2 = ClashRoyaleCardCollection()

        # Crear cartas, meterlas en los decks
        # barajar

        game_state.hand_p1 = ClashRoyaleCardCollection()
        game_state.hand_p2 = ClashRoyaleCardCollection()

        # Poner las cartas en las manos

        game_state.towers_p1 = [500, 1000, 500]
        game_state.towers_p2 = [500, 1000, 500]

        game_state.elixir_p1 = 5
        game_state.elixir_p2 = 5
