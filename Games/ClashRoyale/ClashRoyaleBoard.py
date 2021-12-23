class ClashRoyaleBoard:
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width
        self.board = []

        for r in range(self.board_height):
            row = []
            for c in range(self.board_width):
                row.append(0)
            self.board.append(row)

    def get(self, row, column):
        return self.board[column][row]

    def __str__(self):
        s = ""
        for r in range(self.board_height):
            for c in range(self.board_width):
                if self.is_tower(r, c):
                    s += "*"
                elif self.is_watter(r, c):
                    s += "="
                elif self.is_bridge(r, c):
                    s += " "
                elif self.board[r][c] == 0:
                    s += " "
            s += "\n"
        return s

    def is_tower(self, r, c):
        if (2 <= c <= 4 and 3 <= r <= 5) \
                or (8 <= c <= 10 and 0 <= r <= 2) \
                or (14 <= c <= 16 and 3 <= r <= 5) \
                or (2 <= c <= 4 and 24 <= r <= 26) \
                or (8 <= c <= 10 and 26 <= r <= 28) \
                or (14 <= c <= 16 and 24 <= r <= 26):
            return True
        return False

    def is_watter(self, r, c):
        if r == 14 and c != 4 and c != 14:
            return True
        return False

    def is_bridge(self, r, c):
        if r == 14 and (c == 4 or c == 14):
            return True
        return False
