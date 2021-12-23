from Games.ClashRoyale.ClashRoyaleUnit import ClashRoyaleUnit


class ClashRoyaleBoard:
    def __init__(self, board_height, board_width):
        self.board_height = board_height
        self.board_width = board_width
        self.board = []  # each cell of the boar is of type ClashRoyaleUnit

        self.units = []  # Store a reference to the units included in the board.
        self.last_unit_id = 0

        for r in range(self.board_height):
            row = []
            for c in range(self.board_width):
                row.append(ClashRoyaleUnit())   # empty unit
            self.board.append(row)

    def get_cell(self, row, column):
        return self.board[column][row]

    # Add unit to the board (and units list)
    def add_unit(self, card, r, c, player_id):
        self.board[r][c].assign(self.last_unit_id, player_id, card)
        self.units.append(self.board[r][c])
        self.last_unit_id += 1

    # for printing units information
    def str_units(self):
        s = ""
        for u in self.units:
            if u.player_id == 0:
                str_id = chr(97 + u.unit_id)  # lowercase
            else:
                str_id = chr(65 + u.unit_id)  # capital

            s += str_id + " -> " + str(u) + "\n"
        return s

    def __str__(self):
        s = "--------------------- \n"
        for r in range(self.board_height):
            s += "|"
            for c in range(self.board_width):
                if self.is_tower(r, c):
                    s += "*"
                elif self.is_watter(r, c):
                    s += "="
                elif self.is_bridge(r, c):
                    s += " "
                elif self.board[r][c].is_empty():   # a cell without an unit inside
                    s += " "
                else:
                    s += self.print_cell(r, c)     # a cell with an unit inside
            s += "|\n"
        s += "---------------------"
        return s

    def print_cell(self, r, c):
        s = ""
        if self.board[r][c].player_id == 0:
            s += chr(97 + self.board[r][c].unit_id)  # player 0: lowercase
        else:
            s += chr(65 + self.board[r][c].unit_id)  # player 1: capital
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
