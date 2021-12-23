from Core.ForwardModel import ForwardModel


class ClashRoyaleForwardModel(ForwardModel):
    def play(self, game_state, action, heuristic):
        if action.is_noaction():
            return

        # Deploy new unit
        if game_state.turn == 0:   # top player
            if action.position == "L":
                deploy_r = 7
                deploy_c = 3
            elif action.position == "M":
                deploy_r = 4
                deploy_c = 9
            else:
                deploy_r = 7
                deploy_c = 15
        else:                      # bottom player
            if action.position == "L":
                deploy_r = 22
                deploy_c = 3
            elif action.position == "M":
                deploy_r = 24
                deploy_c = 9
            else:
                deploy_r = 22
                deploy_c = 15

        game_state.add_unit(action.card, deploy_r, deploy_c)

        # TODO: Remove card from hand and apend to deck

        # Mover y/o combatir las tropas en el escenario
        # Actualizar la vida de las torres y unidades
        # Actualizar el maná


    def check_winner(self, game_state):
        # Se gana si:
        # Si no se ha acabado el tiempo y la torre central del otro jugador tiene la vida a cero
        # Si se ha acabado el tiempo, el ganador es:
        # a) El jugador que ha destruido más torres
        # b) Si han destruido el mismo numero de torres, perderá el que tenga la torre con menos vida
        pass
