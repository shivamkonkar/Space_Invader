import pygame

# initialize pygame
pygame.init()

# images
img = pygame.image.load("icons8-space-64.png")
fighter = pygame.image.load("spaceship (1).png")

# create the screen
screen = pygame.display.set_mode((800, 600))

# app title
pygame.display.set_caption("Space Invader")

# setting logo
pygame.display.set_icon(img)

# player
playerX = 370
playerY = 480
fighter_move = 0


def player(x, y):
    screen.blit(fighter, (x, y))


# fighter movement


running = True

while running:
    screen.fill((11, 11, 69))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Keyboard input

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_move = -0.25

            if event.key == pygame.K_RIGHT:
                fighter_move = 0.25

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighter_move = 0

    playerX += fighter_move
    player(playerX, playerY)
    pygame.display.update()

