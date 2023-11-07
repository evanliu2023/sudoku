import pygame
from Board import Board
from Box import Box
from ActionType import ActionType
import util


class GameBoardGui:
    boxes_array: list[list[Box]]
    pygame.init()
    text_size = 50
    text_font = pygame.font.SysFont(name="Arial", size=text_size)
    button_size = 20
    button_font = pygame.font.SysFont(name="Arial", size=button_size)
    BOX_WIDTH = 60
    SCREEN_WIDTH = 580
    SCREEN_HEIGHT = 700
    BOARD_WIDTH = BOX_WIDTH * 9
    BOARD_TOP_MARGIN = 100
    BOARD_LEFT_MARGIN = 20

    # button for Lose
    lose_text_surface = button_font.render('You lose, please click to restart',
                                           True, pygame.Color('steelblue3'))
    lose_col_position = BOARD_TOP_MARGIN + BOX_WIDTH * 9 + 10 + text_size + 10
    # Use this rect for collision detection with the mouse pos.
    lose_button_rect = lose_text_surface.get_rect(topleft=(20, lose_col_position))

    # button for Easy
    easy_text_surface = button_font.render('Easy',
                                           True, pygame.Color('Black'))
    easy_col_position = 60
    # Use this rect for collision detection with the mouse pos.
    easy_button_rect = easy_text_surface.get_rect(topleft=(20, easy_col_position))

    # button for medium
    medium_text_surface = button_font.render('Medium',
                                             True, pygame.Color('Black'))
    medium_col_position = 60
    # Use this rect for collision detection with the mouse pos.
    medium_button_rect = medium_text_surface.get_rect(topleft=(100, medium_col_position))

    # button for hard
    hard_text_surface = button_font.render('Hard',
                                           True, pygame.Color('Black'))
    hard_col_position = 60
    # Use this rect for collision detection with the mouse pos.
    hard_button_rect = hard_text_surface.get_rect(topleft=(200, hard_col_position))

    # button for solve
    solve_text_surface = button_font.render('Solve',
                                            True, pygame.Color('Green'))
    solve_col_position = 60
    # Use this rect for collision detection with the mouse pos.
    solve_button_rect = solve_text_surface.get_rect(topleft=(400, solve_col_position))

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Sudoku")

    def __init__(self, difficulty):
        self.error_count = 0
        self.difficulty = difficulty
        self.board = Board()
        if difficulty is not None:
            self.boxes_array = [[Box(0, 0, 0, 0, 0, 0,
                                     self.screen, self.BOX_WIDTH, False)
                                 for i in range(9)] for j in range(9)]
            self.clock = pygame.time.Clock()
            self.start_time = pygame.time.get_ticks()
            self.my_board = self.board.create_random_board(difficulty)
            # self.board.print_board(self.my_board)
            self.lose_img = pygame.image.load('lose.png').convert_alpha()
            for row in range(0, 9):
                for col in range(0, 9):
                    original = False
                    if self.my_board[row][col] > 0:
                        original = True
                    box = Box(self.my_board[row][col], temp=0,
                              row=row, col=col,
                              x=col * self.BOX_WIDTH + self.BOARD_LEFT_MARGIN,
                              y=row * self.BOX_WIDTH + self.BOARD_TOP_MARGIN,
                              screen=self.screen,
                              box_width=self.BOX_WIDTH,
                              original=original)
                    self.boxes_array[row][col] = box

    def update_boxes_array(self):
        for row in range(0, 9):
            for col in range(0, 9):
                if not self.boxes_array[row][col].original:
                    box = Box(self.my_board[row][col], temp=0,
                              row=row, col=col,
                              x=col * self.BOX_WIDTH + self.BOARD_LEFT_MARGIN,
                              y=row * self.BOX_WIDTH + self.BOARD_TOP_MARGIN,
                              screen=self.screen,
                              box_width=self.BOX_WIDTH,
                              original=False)
                    self.boxes_array[row][col] = box

    def draw_background(self):
        i = 0
        while i < 10:
            if i % 3 == 0:
                line_width = 10
                margin = 4
                color = "blue"
            else:
                line_width = 5
                margin = 0
                color = "black"
            # vertical
            pygame.draw.line(self.screen, color,
                             start_pos=(self.BOX_WIDTH * i + self.BOARD_LEFT_MARGIN,
                                        self.BOARD_TOP_MARGIN - margin),
                             end_pos=(self.BOX_WIDTH * i + self.BOARD_LEFT_MARGIN,
                                      self.BOARD_WIDTH + self.BOARD_TOP_MARGIN + margin),
                             width=line_width)
            # horizontal
            pygame.draw.line(self.screen, color,
                             start_pos=(self.BOARD_LEFT_MARGIN,
                                        self.BOX_WIDTH * i + self.BOARD_TOP_MARGIN),
                             end_pos=(self.BOARD_WIDTH + self.BOARD_LEFT_MARGIN,
                                      self.BOX_WIDTH * i + self.BOARD_TOP_MARGIN),
                             width=line_width)
            i += 1

    def draw_boxes(self):
        for row in range(0, 9):
            for col in range(0, 9):
                box = self.boxes_array[row][col]
                box.draw_box()

    def selected_box(self, position):
        box_row = ((position[1] - self.BOARD_TOP_MARGIN) // self.BOX_WIDTH)
        box_col = ((position[0] - self.BOARD_LEFT_MARGIN) // self.BOX_WIDTH)
        if (self.difficulty is None or box_row > 8
                or box_row < 0
                or box_col > 8
                or box_col < 0):
            return None
        else:
            return self.boxes_array[box_row][box_col]

    def print_timer(self):
        counting_time = pygame.time.get_ticks() - self.start_time

        # change milliseconds into minutes, seconds, milliseconds
        counting_minutes = str(counting_time / 60000).zfill(2)
        counting_seconds = str((counting_time % 60000) / 1000).zfill(2)
        counting_millisecond = str(counting_time % 1000).zfill(3)

        counting_string = "%s:%s:%s" % (counting_minutes, counting_seconds, counting_millisecond)

        counting_text = self.button_font.render(str(counting_string), True, pygame.Color("Black"))
        self.screen.blit(counting_text, (300, 680))
        self.clock.tick(25)

    def print_difficulty_level(self, instruction, color):
        instruction_text_surface = self.button_font.render(instruction,
                                                           True, pygame.Color(color))
        self.screen.blit(instruction_text_surface, (10, 10))
        self.screen.blit(self.easy_text_surface, self.easy_button_rect)
        self.screen.blit(self.medium_text_surface, self.medium_button_rect)
        self.screen.blit(self.hard_text_surface, self.hard_button_rect)
        self.screen.blit(self.solve_text_surface, self.solve_button_rect)

    def repaint(self):
        self.screen.fill("white")
        self.draw_background()

        if self.difficulty is None:
            self.print_difficulty_level("Choose difficulty level to start",
                                        "Black")
        else:
            self.draw_boxes()
            # self.print_timer()

            text = self.text_font.render("X", True, 'red')
            x_range = 3
            if self.error_count <= 3:
                x_range = self.error_count
            for i in range(x_range):
                self.screen.blit(source=text,
                                 dest=(20 + (50 * i),
                                       self.BOARD_TOP_MARGIN + self.BOX_WIDTH * 9 + 10))
            if self.error_count < 3:
                self.print_difficulty_level("Please choose difficulty level to restart",
                                            "Black")
            else:
                self.print_difficulty_level("You lose, please choose difficulty level to restart",
                                            "Red")

    def start_game(self, run):
        print("start_game")
        action = None
        previous_clicked_box = None
        while run:
            key = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        key = 1
                    if event.key == pygame.K_2:
                        key = 2
                    if event.key == pygame.K_3:
                        key = 3
                    if event.key == pygame.K_4:
                        key = 4
                    if event.key == pygame.K_5:
                        key = 5
                    if event.key == pygame.K_6:
                        key = 6
                    if event.key == pygame.K_7:
                        key = 7
                    if event.key == pygame.K_8:
                        key = 8
                    if event.key == pygame.K_9:
                        key = 9
                    if event.key == pygame.K_KP1:
                        key = 1
                    if event.key == pygame.K_KP2:
                        key = 2
                    if event.key == pygame.K_KP3:
                        key = 3
                    if event.key == pygame.K_KP4:
                        key = 4
                    if event.key == pygame.K_KP5:
                        key = 5
                    if event.key == pygame.K_KP6:
                        key = 6
                    if event.key == pygame.K_KP7:
                        key = 7
                    if event.key == pygame.K_KP8:
                        key = 8
                    if event.key == pygame.K_KP9:
                        key = 9
                    if event.key == pygame.K_DELETE:
                        key = None
                    if event.key == pygame.K_RETURN:
                        print("I CLICKED ENTER")
                        print("HIGHLIGHTED BOX", previous_clicked_box.value, previous_clicked_box.temp)
                        # print(self.board.print_board(self.my_board))
                        if previous_clicked_box.temp != 0:
                            if not util.valid(previous_clicked_box.temp,
                                              previous_clicked_box.row,
                                              previous_clicked_box.col,
                                              self.my_board):
                                print("inVALID")
                                self.error_count += 1
                                self.repaint()
                            else:
                                print("VALID")
                                temp_board = util.clone_board(self.my_board)
                                temp_board[previous_clicked_box.row][
                                    previous_clicked_box.col] = previous_clicked_box.temp
                                if self.board.solve(temp_board):
                                    previous_clicked_box.value = previous_clicked_box.temp
                                    self.my_board[previous_clicked_box.row][
                                        previous_clicked_box.col] = previous_clicked_box.value
                                    self.repaint()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    clicked_box = self.selected_box(position)
                    if clicked_box:
                        previous_clicked_box = clicked_box
                        self.repaint()
                        clicked_box.highlight_box()
                    elif event.button == 1:
                        # pressed mouse down on Restart text box
                        if self.lose_button_rect.collidepoint(event.pos):
                            print('lose_button_rect Button pressed.')
                            action = ActionType.RESTART
                            run = False
                        elif self.easy_button_rect.collidepoint(event.pos):
                            # pressed mouse down on Easy text box
                            print('easy_button_rect Button pressed.')
                            action = ActionType.EASY
                            run = False
                        elif self.medium_button_rect.collidepoint(event.pos):
                            # pressed mouse down on Medium text box
                            print('medium_button_rect Button pressed.')
                            action = ActionType.MEDIUM
                            run = False
                        elif self.hard_button_rect.collidepoint(event.pos):
                            # pressed mouse down on Hard text box
                            print('hard_button_rect Button pressed.')
                            action = ActionType.HARD
                            run = False
                        elif self.solve_button_rect.collidepoint(event.pos):
                            # pressed mouse down on Solve text box
                            print('solve_button_rect Button pressed.')
                            self.my_board = self.board.solve_giving_board(self.my_board)
                            util.print_board(self.my_board)
                            self.update_boxes_array()
                            self.repaint()
            if previous_clicked_box and key and previous_clicked_box.value == 0:
                self.boxes_array[previous_clicked_box.row][previous_clicked_box.col].temp = key
                self.repaint()
                previous_clicked_box.highlight_box()

            pygame.display.update()

        return action
