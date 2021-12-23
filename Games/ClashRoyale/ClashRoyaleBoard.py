class ClashRoyaleBoard:
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width
        self.board = []

        for c in range(self.board_width):
            row = []
            for r in range(self.board_height):
                row.append(0)
            self.board.append(row)

    def get(self, row, column):
        return self.board[column][row]

    def __str__(self):
        s = ""
        for c in range(self.board_width):
            for r in range(self.board_height):
                if self.board[c][r] == "0":
                    s += " "
            s += "\n"
        return s
