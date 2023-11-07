import random


def print_board(board):
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


def valid(number, row, column, board):
    if board[row][column] != 0:
        return False
    for col in range(len(board)):
        if number == board[row][col]:
            return False
    for r in range(len(board)):
        if number == board[r][column]:
            return False
    box_row = row // 3
    box_column = column // 3
    for box_r in range(box_row * 3, box_row * 3 + 3):
        for box_col in range(box_column * 3, box_column * 3 + 3):
            if number == board[box_r][box_col]:
                return False
    return True


def pick_empty(board):
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == 0:
                return row, column
    return None


def generate_block(row_number, column_number, board):
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(row_number, row_number + 3):
        for col in range(column_number, column_number + 3):
            num = random.choice(number_list)
            board[row][col] = num
            number_list.remove(num)


def reset_position(board, number):
    for i in range(number):
        row = random.randint(0, 8)
        column = random.randint(0, 8)
        board[row][column] = 0


def reset_board():
    return [
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


def random_generate():
    new_board = reset_board()
    block_list = [0, 3, 6]
    for block in block_list:
        generate_block(block, block, new_board)
    return new_board


def clone_board(board):
    new_board = reset_board()
    for row in range(9):
        for col in range(9):
            new_board[row][col] = board[row][col]
    return new_board
