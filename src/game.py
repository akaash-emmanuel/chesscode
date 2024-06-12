import pygame
from constant import *

class Game:
    def __init__(self):
        pass

    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (0, 0, 0)     #black
                else: 
                    color = (255, 255, 255)       #white

                rectangle = (col * sqsize, row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rectangle)