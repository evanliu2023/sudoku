import pygame
from Board import Board
import button



class Box:
    rows = 9
    columns = 9
    size = 80
    def __init__(self, value, temp, row, col, x, y):
        self.value = value
        self.row = row
        self.col = col
        self.temp = temp
        self.x = x
        self.y = y


    def highlightBox(self):
        pygame.draw.rect(screen, "purple", pygame.Rect(self.x, self.y, self.size, self.size), 10)

    def drawTempNumber(self, temp):
        number = str(temp)
        self.temp = temp
        if number == "0" or number == None:
            number = ""
        text = font.render(number, True, 'grey')
        screen.blit(source=text, dest=(((self.x) + 30), ((self.y) + 20)))

    def drawBox(self):
        pygame.draw.rect(screen, "black", pygame.Rect(self.x, self.y, self.size, self.size), 1)
        number = str(self.value)
        temp = str(self.temp)
        if number != "0":
            text = font.render(number, True, 'black')
        elif temp != "0":
            text = font.render(temp, True, 'grey')
        else:
            text = font.render("", True, 'black')
        screen.blit(source=text, dest=(((self.x) + 30), ((self.y) + 20)))

def drawBackground():
    i = 1
    while i < 9:
        if i % 3 == 0:
            line_width = 10
            color = "blue"
        else:
            line_width = 5
            color = "black"
        pygame.draw.line(screen, color, start_pos= ((80*i), 0), end_pos= (80*i, 720), width=line_width)
        pygame.draw.line(screen, color, start_pos= ((0), 80*i), end_pos= (720, 80*i), width=line_width)
        i+=1

def drawBoxes():
    for row in range(0,9):
        for col in range(0,9):
            box = boxes_array[row][col]
            box.drawBox()

def selectedBox(position):
    if position[1]//80 > 8 or position[0]//80 > 8:
        return None
    box_row = (position[1]//80)
    box_col = (position[0]//80)
    return boxes_array[box_row][box_col]

def repaint():
    screen.fill("white")
    drawBackground()
    drawBoxes()
    text = font.render("X", True, 'red')
    for i in range(error_count):
        screen.blit(source=text, dest=(10+(50*i),730))


pygame.init()
boxes_array = [[Box(0,0,0,0,0,0) for i in range(9)] for j in range(9)]
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")
run = True
error_count = 0
lose_img = pygame.image.load('lose.png').convert_alpha()
board = Board()
my_board = board.createRandomBoard("easy")
board.print_board(my_board)
for row in range(0, 9):
    for col in range(0, 9):
        box = Box(my_board[row][col], temp=0, row=row, col=col, x=col * 80, y=row * 80)
        boxes_array[row][col] = box
font = pygame.font.SysFont(name="Arial",size=50)
repaint()
previous_clicked_box = None

while run:
    key = None
    clickedBox = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
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
                # TODO board.clear()
                key = None
            if event.key == pygame.K_RETURN:
                print("I CLICKED ENTER")
                print("HIGHLIGHTED BOX", previous_clicked_box.value, previous_clicked_box.temp)
                print(board.print_board(my_board))
                if previous_clicked_box.temp != 0:
                   if board.valid(previous_clicked_box.temp, previous_clicked_box.row, previous_clicked_box.col, my_board):
                       print("VALID")
                       temp_board = board.cloneBoard(my_board)
                       temp_board[previous_clicked_box.row][previous_clicked_box.col] = previous_clicked_box.temp
                       if board.solve(temp_board):
                           previous_clicked_box.value = previous_clicked_box.temp
                           my_board[previous_clicked_box.row][previous_clicked_box.col] = previous_clicked_box.value
                           repaint()
                   else:
                       print("Invalid")
                       error_count += 1
                       repaint()
                       if error_count >= 3:
                           lose_button = button.Button(200, 300, lose_img, 0.5)
                           lose_button.draw(screen)
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            clickedBox = selectedBox(position)
        if clickedBox:
            previous_clicked_box = clickedBox
            repaint()
            clickedBox.highlightBox()
    if previous_clicked_box and key and previous_clicked_box.value == 0:
        boxes_array[previous_clicked_box.row][previous_clicked_box.col].temp = key
        repaint()
        previous_clicked_box.highlightBox()

    pygame.display.update()
