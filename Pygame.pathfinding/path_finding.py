import pygame

screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_width))

white = (255, 255, 255)
red = (0, 255, 0)
grey = (128, 128, 128)


class Spot:
    def __init__(self, row, col, width, height):
        self.row = row
        self.col = col
        self.width = row * width
        self.height = col * width
        self.color = white
        self.neightbors = []
        self.width = width
    # Eod
# Eoc


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # Eoi
        # Eof
    # Eow
# Eom


main()
