# importing packages
import pygame
from pygame.locals import *
import sys
import random

# 2 Defining constants
BLACK_WIDTH = 640
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load('images/ball.png')
# sound for bounce
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
# sound for play background
pygame.mixer.music.load('sounds/sound_back.mp3')
pygame.mixer.music.play(-1, 0.0)
# 5 - Initialize variables
ballRect = ballImage.get_rect()
print(ballRect)
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed
        bounceSound.play()
    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed
        bounceSound.play()
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed
    window.fill(BLACK)
    window.blit(ballImage, ballRect)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
