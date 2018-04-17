import random

class TicTacToe:
    def __init__(self, **fields):
        self.plyrs = {fields.pop("X", "ai"): "X", fields.pop("O", "ai"): "O"}
        self.winner = None
        self.board = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

    def check(self, b):
        #horizontal check
        if ((b[0][0] == "O" and b[0][1] == "O" and b[0][2] == "O") or (b[1][0] == "O" and b[1][1] == "O" and b[1][2] == "O")) or ((b[2][0] == "O" and b[2][1] == "O" and b[2][2] == "O") or (b[0][0] == "X" and b[0][1] == "X" and b[0][2] == "X") or (b[1][0] == "X" and b[1][1] == "X" and b[1][2] == "X") or (b[2][0] == "X" and b[2][1] == "X" and b[2][2] == "X")):
            return True

        #vertical check
        if ((b[0][0] == "O" and b[1][0] == "O" and b[2][0] == "O") or (b[0][1] == "O" and b[1][1] == "O" and b[2][1] == "O")) or ((b[0][2] == "O" and b[1][2] == "O" and b[2][2] == "O") or (b[0][0] == "X" and b[1][0] == "X" and b[2][0] == "X") or (b[0][1] == "X" and b[1][1] == "X" and b[2][1] == "X") or (b[0][2] == "X" and b[1][2] == "X" and b[2][2] == "X")):
            return True

        #diagonal check
        if ((b[0][0] == "O" and b[1][1] == "O" and b[2][2] == "O") or (b[0][2] == "O" and b[1][1] == "O" and b[2][0] == "O")) or ((b[0][0] == "X" and b[1][1] == "X" and b[2][2] == "X") or (b[0][2] == "X" and b[1][1] == "X" and b[2][0] == "X")):
            return True

        return False

    def board_full(self):
        board_list = []
        for row in self.board:
            board_list += row

        return set(board_list) == {"O", "X"} or set(board_list) == {"X", "O"}

    def print_board(self):
        msg = []
        for x in self.board:
            msg.append(" {} | {} | {} \n".format(x[0], x[1], x[2]))

        return "------------\n".join(msg)

    def comp_move(self):
        #check if any of our moves can win
        for row in self.board:
            for e in row:
                if e not in ["O", "X"]:
                    num = int(e)
                    copy_b = [x.copy() for x in self.board]
                    copy_b[self.board.index(row)][row.index(e)] = "X"
                    if self.check(copy_b):
                        return num

        #check if any of the enemy moves can win
        for row in self.board:
            for e in row:
                if e not in ["O", "X"]:
                    num = int(e)
                    copy_b = [x.copy() for x in self.board]
                    copy_b[self.board.index(row)][row.index(e)] = "O"
                    if self.check(copy_b):
                        return num

        #take the center
        if not self.board[1][1] in ["X", "O"]:
            return 5

        #take a random corner
        choices = []
        for corner in [1, 3, 7, 9]:
            if not self.board[int(corner//3.5)][(corner-1)%3] in ["X", "O"]:
                choices.append(corner)

        if len(choices) > 0:
            return random.choice(choices)

        choice = []
        #take a random side
        for side in [2, 4, 6, 8]:
            if not self.board[int(side//3.5)][(side-1)%3] in ["X", "O"]:
                choices.append(side)

        if len(choices) > 0:
            return random.choice(choices)

    def validate(self, value):
        if not isinstance(value, int):
            try:
                value = int(value)
            except ValueError:
                return False

        if value < 1 or value > 9:
            return False

        if self.board[int(value//3.5)][(value-1)%3] in ["X", "O"]:
            return False

        return True

    def game_over(self):
        return self.board_full() or self.check(self.board)

    def play(self, player, value=None):
        if not player in self.plyrs.keys():
            raise ValueError("Must be one of the two players")

        if player == "ai":
            value = self.comp_move()

        if self.validate(value):
            value = int(value)
            self.board[int(value//3.5)][(value-1)%3] = self.plyrs[player]

        if self.check(self.board):
            self.winner = player

        return value



            

