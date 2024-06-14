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
        dragger = self.game.dragger
        board = self.game.board

        while True:
            game.show_bg(scr)
            game.show_pieces(scr)

            if dragger.dragging:
                dragger.update_blit(scr)

            for event in pygame.event.get():     

                if event.type == pygame.MOUSEBUTTONDOWN:            #click event
                    dragger.update_mouse(event.pos)                 #the position of the click in cartesian coords

                    clicked_row = dragger.Y // sqsize               #row based on coords
                    clicked_col = dragger.X // sqsize               #col based on coords

                    if board.squares[clicked_row][clicked_col].has_piece():         #to check if the clicked square has a piece
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)                         #to not drag an empty square
                        dragger.drag_piece(piece)

                elif event.type == pygame.MOUSEMOTION:              #moving the mouse
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(scr)
                
                elif event.type == pygame.MOUSEBUTTONUP:            #unclick event
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT:                     #quit 
                    pygame.quit()
                    sys.exit()
            

            pygame.display.update()
        

main = Main()               # instances of the object
main.mainloop()
