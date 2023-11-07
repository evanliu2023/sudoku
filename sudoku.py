import random
import util


def pick_empty(board):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                return row, column
    return None


def solve(board):
    position = pick_empty(board)
    if not position:
        return True
    for number in range(1, 10):
        if util.valid(number, position[0], position[1], board):
            board[position[0]][position[1]] = number
            if solve(board):
                return True
            board[position[0]][position[1]] = 0
    return False


def random_generate():
    new_board = util.reset_board()
    block_list = [0, 3, 6]
    for block in block_list:
        util.generate_block(block, block, new_board)
    return new_board


def solve_generated():
    board = random_generate()
    solve(board)
    return board


def create_random_board(difficulty):
    board = solve_generated()
    if difficulty == "easy" or difficulty == "Easy":
        reset_position(board, 21)
    if difficulty == "medium" or difficulty == "Medium":
        reset_position(board, 41)
    if difficulty == "hard" or difficulty == "Hard":
        reset_position(board, 61)
    return board


def reset_position(board, number):
    for i in range(number):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        board[row][column] = 0


def play(difficulty):
    board = create_random_board(difficulty)
    util.print_board(board)
    solve(board)
    print()
    util.print_board(board)


difficulty_level = input("Enter difficulty")
play(difficulty_level)
