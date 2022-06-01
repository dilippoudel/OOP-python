import pygame
from pygame.locals import *
import sys
import random
from Ball import *

# Defining constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 960
FRAMES_PER_SECOND = 30
N_BALLS = 20
# INITIALIZING THE WORLD
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
ballList = []
print(ballList)
for oBall in range(0, N_BALLS):
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)


# Loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for oBall in ballList:
        oBall.update()
    window.fill(BLACK)
    for oBall in ballList:
        oBall.draw()


    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
