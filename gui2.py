import pygame
from GameBoardGui import GameBoardGui
from ActionType import ActionType


# entry file point to start a sudoku game

# start a new game by giving difficulty
def start(difficulty):
    game_board_gui = GameBoardGui(difficulty=difficulty)
    game_board_gui.repaint()
    return game_board_gui.start_game(True)


# init the game board
pygame.init()
action = ActionType.START
run = True

# listen on the action type to start a new game
while run:
    if action == ActionType.START:
        action = start(None)
    elif action == ActionType.EASY:
        action = start(action)
    elif action == ActionType.MEDIUM:
        action = start(ActionType.MEDIUM)
    elif action == ActionType.HARD:
        action = start(ActionType.HARD)
    else:
        run = False
