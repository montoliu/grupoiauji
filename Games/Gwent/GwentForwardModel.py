from Core.ForwardModel import ForwardModel


class GwentForwardModel(ForwardModel):

    def play(self, game_state, action, heuristic):
        actual_player = game_state.turn

        card = action.get_card()

        game_state.hands[actual_player].remove(card)

        if actual_player == 0:
            game_state.terrain_p1.add_card(card)
        elif actual_player == 1:
            game_state.terrain_p2.add_card(card)

    def get_round_winner(self, game_state):
        if game_state.points_p1 > game_state.points_p2:
            return 1
        elif game_state.points_p1 < game_state.points_p2:
            return 2
        else:  # The round is a draw
            return 0

    def check_winner(self, game_state):
        if game_state.lives_p1 == 0:
            game_state.winner = 2
        elif game_state.live_p2 == 0:
            game_state.winner = 1
