# Libraries
import pygame

# Initialice the game
pygame.init

# Colors
background = (0, 0, 0)
white = (255, 255, 255)

# Variables
running = True

# Screen
width = 600
height = 600
size = (width, height)
screen = pygame.display.set_mode(size)


def draw_rectangle(color, position):
    print(position)
    x = position[0] - 10
    y = position[1] - 10
    pygame.draw.rect(screen, color, (x, y, 20, 20))
# Eod


while running:
    # Check for the events in the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Eoi
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # When left click is pressed
            draw_rectangle(white, mouse)
        # Eoi
        if pygame.mouse.get_pressed()[2]:  # When right click is pressed
            draw_rectangle(background, mouse)
        # Eoi
    # Eof

    # Update the display each time
    pygame.display.flip()

# Eow
