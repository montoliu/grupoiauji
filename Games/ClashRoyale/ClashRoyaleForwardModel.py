from Core.ForwardModel import ForwardModel


class ClashRoyaleForwardModel(ForwardModel):
    def play(self, game_state, action, heuristic):
        # Deploy la tropa que diga la action
        # Mover y/o combatir las tropas en el escenario
        # Actualizar la vida de las torres y unidades
        # Actualizar el maná
        pass

    def check_winner(self, game_state):
        # Se gana si:
        # Si no se ha acabado el tiempo y la torre central del otro jugador tiene la vida a cero
        # Si se ha acabado el tiempo, el ganador es:
        # a) El jugador que ha destruido más torres
        # b) Si han destruido el mismo numero de torres, perderá el que tenga la torre con menos vida
        pass
