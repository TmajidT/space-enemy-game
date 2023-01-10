import time
import pygame
import random
from pygame import mixer


# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("b59dd4c3-4bfe-471d-9b66-52d798283b8c.png")

# Title and Icon
pygame.display.set_caption("space Invaders")
icon = pygame.image.load("space-shuttle.png")
pygame.display.set_icon(icon)

# Player position
PlayerImg = pygame.image.load("icons8-babylon-5-centauri-ship-48.png")
PlayerX = 370
PlayerY = 400
PlayerX_change = 0
PlayerY_change = 0

# enemy position
EnemyImg = pygame.image.load("icons8-alien-monster-emoji-48.png")
EnemyX = random.randint(0, 600)
EnemyY = random.randint(0, 400)
EnemyX_change = 0.6
EnemyY_change = 0.6

# arrow position
ArrowImg = pygame.image.load("icons8-archers-arrow-64 (1).png")
ArrowX = 0
ArrowY = 0
ArrowX_change = 0
ArrowY_change = 5
Arrow_state = "ready"  # ready means you can't see the bullet

# play the sound
mixer.init()
mixer.music.load("boom-sound.mp3")
mixer.music.set_volume(0.2)

bang_icon = pygame.image.load("icons8-bang-48.png")

def player(x, y):
    # draw img on screen
    screen.blit(PlayerImg, (x, y))


def enemy(x, y):
    screen.blit(EnemyImg, (x, y))


def fire_arrow(x, y):
    global Arrow_state
    Arrow_state = "fire"  # fire means arrow in being shootet
    screen.blit(ArrowImg, (x - 9, y - 10))

def kill_enemy(x, y):
    screen.blit(bang_icon, (x + 50, y))
    screen.blit(bang_icon, (x - 40, y - 50))
    # Play the music
    mixer.music.play()


# game loop
running = True
while running:

    # RGB = red , green , blue
    screen.fill((150, 0, 150))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check is its right or left(keydown is preesing a key)
        if event.type == pygame.KEYDOWN:
            print("a key stroke has been pressed")
            if event.key == pygame.K_LEFT:
                PlayerX_change = -0.9
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 0.9
            if event.key == pygame.K_UP:
                PlayerY_change = -0.9
            if event.key == pygame.K_DOWN:
                PlayerY_change = 0.9
            if event.key == pygame.K_SPACE:
                if Arrow_state == "ready":
                    fire_arrow(PlayerX, PlayerY)
                    ArrowX = PlayerX
                    ArrowY = PlayerY

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                PlayerX_change = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                PlayerY_change = 0

    PlayerX += PlayerX_change
    # check if the player is inside the zone
    if PlayerX < 0:
        PlayerX = 0
    elif PlayerX > 750:
        PlayerX = 750
    PlayerY += PlayerY_change
    if PlayerY > 550:
        PlayerY = 550
    elif PlayerY < 350:
        PlayerY = 350

    EnemyX += EnemyX_change
    EnemyY += EnemyY_change

    if EnemyX < 0:
        EnemyX_change = 0.6
    elif EnemyX > 750:
        EnemyX_change = -0.6
    if EnemyY < 0:
        EnemyY_change = 0.6
    elif EnemyY > 550:
        EnemyY_change = -0.6

    #ArrowX = PlayerX
    #ArrowY = PlayerY
    # Bullet movement
    if Arrow_state == "fire":
        fire_arrow(ArrowX, ArrowY)
        ArrowY = ArrowY - ArrowY_change
        if ArrowY < 0:
            Arrow_state = "ready"




    #after you pressed space
    if Arrow_state == "fire":
        if (ArrowY < EnemyY + 10) and (ArrowY > EnemyY - 10) and (ArrowX < EnemyX + 20) and (ArrowX > EnemyX - 20):
            Arrow_state = "ready"
            kill_enemy(ArrowX,ArrowY)



    player(PlayerX, PlayerY)
    enemy(EnemyX, EnemyY)

    # update screen
    pygame.display.update()
