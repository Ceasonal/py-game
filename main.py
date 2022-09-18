import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title & Icon
pygame.display.set_caption("Asteroid Defense")
icon = pygame.image.load("gameimg/spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("gameimg/shipmain.png")
playerX = 370
playerY = 480
playerX_change = 0


# Asteroids
asteroidImg = pygame.image.load("gameimg/asteroid.png")
asteroidX = random.randint(0, 800)
asteroidY = random.randint(50, 50)
asteroidX_change = 0.3
asteroidY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def astroid(x, y):
    screen.blit(asteroidImg, (x, y))


# Game Loop
running = True
while running:
    # RGB Color
    screen.fill((0, 0, 0))
    # playerX += 0.1 #makes img move right auto

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            # print("A keystore is pressed")#if any other keystore is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                # print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                # print("Keystore has been released")

    playerX += playerX_change  # move player position
    if playerX <= 0:  # create/set boundaries
        playerX = 0
    elif playerX >= 737:  # ship width = 800-63 =737
        playerX = 737

    asteroidX += asteroidX_change  # enemy movement
    if asteroidX <= 0:  # create/set boundaries
        asteroidX_change = 0.3
        asteroidY += asteroidY_change
    elif asteroidX >= 736:  # astroid width = 800-64 =736
        asteroidX_change = -0.3
        asteroidY += asteroidY_change

    player(playerX, playerY)
    astroid(asteroidX, asteroidY)
    pygame.display.update()

print("hi")