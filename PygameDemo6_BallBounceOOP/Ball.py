import pygame
from pygame import *
import random
import sys


# Ball class

class Ball:
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image = pygame.image.load('images/ball.png')
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)
        speedList = [-4, -3, -3, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedList)
        self.ySpeed = random.choice(speedList)

    def update(self):
        if (self.x <= 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed
        if (self.y <= 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed
        # updating the ball's x and y position
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
        
