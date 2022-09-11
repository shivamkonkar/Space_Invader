import pygame
import random
import math

from pygame import mixer

# initialize pygame
pygame.init()
pygame.mixer.init()

enemy = []
enemyX = []
enemyY = []
enemyX_move = []
enemyY_move = []
number_of_enemies = 10

# images
bgImg = pygame.image.load("wepik-purple-space-stars-desktop-wallpaper-2022811-144342.png")
img = pygame.image.load("icons8-space-64.png")
fighter = pygame.image.load("spaceship (1).png")

bullet = pygame.image.load("bullet (1).png")

# bgsound

mixer.music.load("alt-J_-_Worlds_Smallest_Violin.wav")
mixer.music.play(-1)

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


# enemy

for i in range(number_of_enemies):
    enemy.append(pygame.image.load("asteroid.png"))
    enemyX.append(random.randint(0, 770))
    enemyY.append(50)
    enemyX_move.append(0.7)
    enemyY_move.append(40)

def ai(x, y):
    screen.blit(enemy[i], (x, y))


# bullet

bulletY = 455
bulletY_move = 5
bullet_state = "ready"
bullet_loc = 0


# shoot function
def shoot(x, y):

    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 16))



# collision function
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if (distance < 25):
        return True
    else:
        return False


# Score
score = 0
font = pygame.font.Font("FreeSansBold.ttf",32)
overFont = pygame.font.Font("FreeSansBold.ttf",64)
textX = 10
textY = 10

def show_score(x , y):
    scoreV = font.render("Score :" + str(score), True , (255,255,255))
    screen.blit(scoreV,(x,y))

def game_over_text():

    mixer.music.stop()
    gameOverSound = mixer.Sound("cute-pixie-says-game-over-83489.wav")
    gameOverSound.play()
    finalScore = overFont.render("GAMEOVER",True,(255,255,255))
    screen.blit(finalScore,(200,250))

running = True

while running:
    screen.blit(bgImg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard input

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_move = -0.95

            if event.key == pygame.K_RIGHT:
                fighter_move = 0.95

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_loc = bulletX
                    shoot(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fighter_move = 0

    playerX += fighter_move

    # checking for border

    if playerX < 0:
        playerX = 0

    if playerX > 730:
        playerX = 730

    # Bullet Movement

    if bullet_state == "fire":
        shoot(bulletX, bulletY)

        bulletY -= bulletY_move

    if bulletY <= 0:
        bulletY = 455
        bullet_state = "ready"

# enemies movement and collision
    for i in range(number_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        if enemyX[i] < 0:
            enemyX_move[i] = 1.35
            enemyY[i] += enemyY_move[i]

        if enemyX[i] > 750:
            enemyX_move[i] = -1.35
            enemyY[i] += enemyY_move[i]

        enemyX[i] += enemyX_move[i]



    # collision

        collision = isCollision(enemyX[i], enemyY[i], bullet_loc, bulletY)
        if collision:

            bulletY = 455
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 700)
            enemyY[i] = 50
            explosion = mixer.Sound("muffled-distant-explosion-7104.wav")
            explosion.play()

        ai(enemyX[i], enemyY[i])

    show_score(textX,textY)
    player(playerX, playerY)
    pygame.display.update()
