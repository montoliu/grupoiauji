class ClashRoyaleBoard:
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width
        self.board = []

        self.units_p1 = []
        self.units_p2 = []

        self.last_p1 = "1"
        self.last_p2 = "a"

        for r in range(self.board_height):
            row = []
            for c in range(self.board_width):
                row.append(" ")
            self.board.append(row)

    def get(self, row, column):
        return self.board[column][row]

    def add_unit(self, unit, r, c, player_id):
        if player_id == 0:
            self.board[r][c] = self.last_p1
            self.units_p1.append(unit)
            self.last_p1 = self.next_char_p1(self.last_p1)
        else:
            self.board[r][c] = self.last_p2
            self.units_p2.append(unit)
            self.last_p2 = self.next_char_p2(self.last_p2)

    def next_char_p1(self, value):
        if value == "1":
            return "2"
        if value == "2":
            return "3"
        if value == "3":
            return "4"
        if value == "4":
            return "5"

    def next_char_p2(self, value):
        if value == "a":
            return "b"
        if value == "b":
            return "c"
        if value == "c":
            return "d"
        if value == "d":
            return "e"

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
                elif self.board[r][c] == " ":
                    s += " "
                else:
                    s += self.board[r][c]
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
