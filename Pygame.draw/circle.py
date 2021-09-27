# Libraries to import
import pygame

# Initilize the game
pygame.init

# Game colors
white = [255, 255, 255]
black = [0, 0, 0]

# Size of the window
width = 500
heigth = 500
size = (width, heigth)
# Set the size of the screen
screen = pygame.display.set_mode(size)

flag = True


def draw_circle(tup, color):
    global flag
    if color != black and flag:
        color[1] -= 1
    elif flag == False:
        color[1] += 1

    if color[1] < 0 and flag:
        color[1] = 0
        flag = False
    if color[1] > 255 and flag == False:
        color[1] = 255
        flag = True

    pygame.draw.circle(screen, color, tup, 10)

    print(color, flag)
    pygame.display.flip()


# Loop to get the game running
running = True
while running:
    # Check if the event is to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Eoi
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            rightButton = mouse
            draw_circle(rightButton, white)
        # Eoi
        if pygame.mouse.get_pressed()[2]:
            leftButton = mouse
            draw_circle(leftButton, black)
    # Eof

    # Update the display
    pygame.display.flip()

# Eow
