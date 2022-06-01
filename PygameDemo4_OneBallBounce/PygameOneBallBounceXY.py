# Importing packages
import pygame
from pygame import *
import sys
import random

# Defining constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3
# Initializing world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
# 4. Load assets
ballImage = pygame.image.load('images/ball.png')
# Initializing variables
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballX = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
ballY = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
# 6 Loop Forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 8 - Do any "per frame" actions
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed  # reverse x direction
    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed
    # update the ball location
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    # 9 clear the window before drawing  it again
    window.fill(BLACK)
    # 10 Draw the window elements
    window.blit(ballImage, (ballX, ballY))
    # 11 update the window
    pygame.display.update()
    # 12 slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
