from Core.Game import Game


class ClashRoyaleGame(Game):
    def reset(self, game_state, player_id_as_first):
        game_state.reset(player_id_as_first)
