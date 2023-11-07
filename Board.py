import util


class Board:

    def __call__(self):
        return self

    def solve(self, board):
        position = util.pick_empty(board)
        if not position:
            return True
        for number in range(1, 10):
            if util.valid(number, position[0], position[1], board):
                board[position[0]][position[1]] = number
                if self.solve(board):
                    return True
                board[position[0]][position[1]] = 0
        return False

    def solve_generated(self):
        board = util.random_generate()
        self.solve(board)
        return board

    def solve_giving_board(self, board):
        self.solve(board)
        return board

    def create_random_board(self, difficulty):
        board = self.solve_generated()
        if difficulty == "easy" or difficulty == "Easy":
            util.reset_position(board, 31)
        if difficulty == "medium" or difficulty == "Medium":
            util.reset_position(board, 41)
        if difficulty == "hard" or difficulty == "Hard":
            util.reset_position(board, 61)
        return board

    def play(self, difficulty):
        board = self.create_random_board(difficulty)
        util.print_board(board)
        self.solve(board)
        print()
        util.print_board(board)
