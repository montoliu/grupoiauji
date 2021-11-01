# An observation is the allowed view of the game state for the players
# It is a copy of the game state but just the elements that the player can see.
# For the elements that the player cannot see (.e.g. the other player hand),
#    it has a randomized version of the elements.
class Observation:
    def get_list_actions(self):
        pass

    def clone(self):
        pass
