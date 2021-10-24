from Core.Action import Action


# An action is just the row and column where the player plays
class TicTacToeAction(Action):
    def __init__(self, row, column):
        self.column = column
        self.row = row

    def __str__(self):
        return "" + str(self.row) + " " + str(self.column)
