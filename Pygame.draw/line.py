# Libraries
import pygame

# Global variables
pygame.init

width = 600
height = 600
window_size = (width + 1, height + 1)
screen = pygame.display.set_mode(window_size)

blue = (0, 0, 255)
white = (255, 255, 255, 0.6)

running = True


# Funcitons


def draw_grid():
    gap = 30
    for i in range(width):
        pygame.draw.line(screen, white, (0, i * gap), (width, i * gap))
        for j in range(width):
            pygame.draw.line(screen, white, (j * gap, 0), (j * gap, width))
        # EOF
    # EOF
# EOF


# Game it self
while running:
    for event in pygame.event.get():
        # Event to exit the game
        if event.type == pygame.QUIT:
            running = False
        # EOI
    # EOF

    # Draw lines in the screen
    draw_grid()

    # Update the display every frame
    pygame.display.update()

# EOW
