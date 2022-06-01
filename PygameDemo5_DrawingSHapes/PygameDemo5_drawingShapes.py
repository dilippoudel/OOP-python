import pygame
from pygame import *
import random
import sys

GRAY = (0, 128, 128)
BLUE = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3
# Initializing world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# loop forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill(GRAY)
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)
    pygame.draw.circle(window, GREEN, (400, 50), 30, 0)
    pygame.draw.circle(window, RED, (60, 200), 50, 2)
    pygame.draw.circle(window, YELLOW, (90, 100), 30, 4)
    pygame.draw.polygon(window, YELLOW, ((240, 350), (350, 350), (410, 410), (350, 470), (240, 470), (170, 410)))
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 1, 5)
    pygame.draw.lines(window, BLUE, True, [(150, 200), (250, 200), (250, 300), (300, 250)], 2)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
