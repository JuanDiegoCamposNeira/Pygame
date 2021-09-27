import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen for the game
min_width = 0
max_width = 800
min_heigth = 0
max_heigth = 600
screen = pygame.display.set_mode((max_width, max_heigth))  # ( x, y )

# Background image
background = pygame.image.load("background.jpg")

#                   NAME AND ICON
# Name
pygame.display.set_caption("Space Invaders")
# Icon
# This line charges up an image to the game
icon = pygame.image.load("spaceship.png")
# This line sets the image 'icon' to the icon of the game
pygame.display.set_icon(icon)
# Other way to do it is by doing the following:
# pygame.display.set_icon( pygame.image.load("image.png") ) // Do not work propetly in linux

#                   PLAYER
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):  # Funtion that will draw the image of the player into the screen
    # .blit( image_to_load, (x, y) ) will draw into the screen
    screen.blit(playerImage, (x, y))
# EOD


#                   ENEMY
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.3
enemyY_change = 40


def enemy(x, y):  # Function to draw the enemies into the screen
    screen.blit(enemyImg, (enemyX, enemyY))
# Eod


#                    BULLETS
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40


# Event variable to quit the game
running = True
# Game loop
while running:
    # Change the background of the color
    screen.fill((143, 23, 183))  # RGB value for background

    # Change the background image
    # screen.blit(background, (0, 0))

    # Loop to get every event in the game
    for event in pygame.event.get():
        # If the event is the mouse, draw a line or an image
        mouse = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:  # When the exit button is pressed
            running = False
        # Eoi

        # Event for when the keystroke is pressed down
        if event.type == pygame.KEYDOWN:  # When any key is pressed down
            if event.key == pygame.K_RIGHT:
                playerX_change += 0.5
            # Eoi
            if event.key == pygame.K_LEFT:
                playerX_change -= 0.5
            # Eoi
        # Eoi
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            # Eoi
    # EOF

    #                   PLAYER
    # Position the player into the screen
    # Increse/decrese the value of the X coordinate
    playerX += playerX_change

    # Boundaries of the game
    if playerX < min_width:
        playerX = min_width
    # Eoi
    elif playerX > max_width - 64:
        playerX = max_width - 64
    # Eoei

    #                   ENEMY
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
        # Eoi
    elif enemyX >= max_width - 64:
        enemyX_change = -0.3
        enemyY += enemyY_change
    # Eoei

    # Call the function to draw the player
    player(mouse[0] - 32, mouse[1] - 32)
    player(playerX, playerY)
    enemy(enemyX, enemyY)  # Call the function to draw the enemies

    # The game window is always updating with the configuration inside of the while loop
    pygame.display.update()

# EOW
