# pygame 2 demo - one  image, click and move
# 1 import packages
import pygame
from pygame import *
import sys
import random

# 2 Defining constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

# 3 Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 load assests
ballImage = pygame.image.load('./images/ball.png')

# initialize variable
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# 6 - Loop forever
while True:
    # 7 check for and handle events
    for event in pygame.event.get():

        # clicked the close button and quit the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT)
    window.fill(BLACK)
    # Draw the ball at the randomized location
    window.blit(ballImage, (ballX, ballY))
    # update the window
    pygame.display.update()
    # slow things down a bit
    clock.tick(FRAMES_PER_SECOND)
# mouseX, MouseY = event.pos
