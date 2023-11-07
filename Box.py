import pygame


class Box:
    left_margin = 100
    top_margin = 100
    right_margin = 100
    rows = 9
    columns = 9
    pygame.init()
    FONT_SIZE = 40
    FONT_MARGIN = 10
    font = pygame.font.SysFont(name="Arial", size=FONT_SIZE)

    def __call__(self):
        return self

    def __init__(self, value, temp, row, col, x, y, screen, box_width, original):
        self.value = value
        self.row = row
        self.col = col
        self.temp = temp
        self.x = x
        self.y = y
        self.screen = screen
        self.box_width = box_width
        self.original = original

    def highlight_box(self):
        pygame.draw.rect(self.screen, "purple",
                         pygame.Rect(self.x, self.y, self.box_width, self.box_width), 10)

    def draw_temp_number(self, temp):
        number = str(temp)
        self.temp = temp
        if number == "0" or number is None:
            number = ""
        text = self.font.render(number, True, 'grey')
        self.screen.blit(source=text, dest=((self.x + self.FONT_MARGIN), (self.y + self.FONT_MARGIN)))

    def draw_box(self):
        pygame.draw.rect(self.screen, "black",
                         pygame.Rect(self.x, self.y, self.box_width, self.box_width), 1)
        number = str(self.value)
        temp = str(self.temp)
        if number != "0":
            if self.original:
                text = self.font.render(number, True, 'black')
            else:
                text = self.font.render(number, True, 'Green')
        elif temp != "0":
            text = self.font.render(temp, True, 'grey')
        else:
            text = self.font.render("", True, 'black')
        self.screen.blit(source=text, dest=((self.x + self.FONT_MARGIN), (self.y + self.FONT_MARGIN)))
