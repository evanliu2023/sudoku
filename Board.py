import random

class Board:

    def __call__(self):
        return self


    def print_board(self, board):
        for i in range(len(board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - - - -")
            for j in range(len(board)):
                if j % 3 == 0 and j != 0:
                    print("|", " ", end="")
                if j == 8:
                    print(board[i][j])
                else:
                    print(board[i][j], " ", end="")


    def pick_empty(self, board):
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] == 0:
                    return (row, column)
        return None


    def valid(self, number, row, column, board):
        if board[row][column] != 0:
            return False
        for col in range(len(board)):
            if number == board[row][col]:
                return False
        for r in range(len(board)):
            if number == board[r][column]:
                return False
        box_row = row//3
        box_column = column//3
        for box_r in range(box_row*3, box_row*3 + 3):
            for box_col in range(box_column*3, box_column*3 +3):
                if number == board[box_r][box_col]:
                    return False
        return True

    def solve(self, board):
        position = self.pick_empty(board)
        if not position:
            return True
        for number in range(1,10):
            if self.valid(number, position[0], position[1], board):
                board[position[0]][position[1]] = number
                if self.solve(board):
                    return True
                board[position[0]][position[1]] = 0
        return False

    def cloneBoard(self, board):
        new_board = self.resetBoard()
        for row in range(9):
            for col in range(9):
                new_board[row][col] = board[row][col]
        return new_board


    def resetBoard(self):
        reset = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        return reset


    def randomGenerate(self):
        new_board = self.resetBoard()
        block_list = [0, 3, 6]
        for block in block_list:
            self.generateBlock(block, block, new_board)
        return(new_board)

    def generateBlock(self, row_number, column_number, board):
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(row_number, row_number+3):
            for col in range(column_number, column_number+3):
                num = random.choice(number_list)
                board[row][col] = num
                number_list.remove(num)


    def solveGenerated(self):
        board = self.randomGenerate()
        self.solve(board)
        return board


    def createRandomBoard(self, difficulty):
        board = self.solveGenerated()
        if difficulty == "easy" or difficulty == "Easy":
            self.resetPosition(board,31)
        if difficulty == "medium" or difficulty == "Medium":
            self.resetPosition(board,41)
        if difficulty == "hard" or difficulty == "Hard":
            self.resetPosition(board,61)
        return board


    def resetPosition(self, board, number):
        for i in range(number):
            row = random.randint(0, 8)
            column = random.randint(0, 8)
            board[row][column] = 0


    def play(self, difficulty):
        board = self.createRandomBoard(difficulty)
        self.print_board(board)
        self.solve(board)
        print()
        self.print_board(board)


