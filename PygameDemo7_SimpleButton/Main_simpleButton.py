import sys

import pygame
from pygame.locals import *

from PygameDemo7_SimpleButton.SimpleButton import SimpleButton

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
clock = pygame.time.Clock()

# INITIALIZING THE WORLD
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

oButton = SimpleButton(window, (150, 30), 'images/start.png', 'images/exit.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if oButton.handleEvent(event):
            print('user has clicked')
    window.fill(BLACK)
    oButton.draw()
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)