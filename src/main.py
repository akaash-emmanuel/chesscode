import pygame
import sys

from constant import *
from game import Game

class Main:
    def __init__(self):      # objects being created 
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))      # a screen is created in a variable self.screen
        pygame.display.set_caption('ChessGame')      # name
        self.game = Game()
    def mainloop(self):

        game = self.game
        scr = self.screen

        while True:
            self.game.show_bg(self.screen)
            for event in pygame.event.get():     # to close game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            

            pygame.display.update()
        

main = Main()               # instances of the object
main.mainloop()
