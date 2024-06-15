import pygame
import sys

from constant import *
from game import Game
from square import Square
from move import Move

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
            game.show_last_move(scr)
            game.show_moves(scr)
            game.show_pieces(scr)
            game.show_hover(scr)

            if dragger.dragging:
                dragger.update_blit(scr)

            for event in pygame.event.get():     

                if event.type == pygame.MOUSEBUTTONDOWN:            #click event
                    dragger.update_mouse(event.pos)                 #the position of the click in cartesian coords

                    clicked_row = dragger.Y // sqsize               #row based on coords
                    clicked_col = dragger.X // sqsize               #col based on coords

                    if board.squares[clicked_row][clicked_col].has_piece():         #to check if the clicked square has a piece
                        piece = board.squares[clicked_row][clicked_col].piece
                        if piece.color == game.next_player:
                            board.calc_moves(piece, clicked_row, clicked_col, bool = True)

                            dragger.save_initial(event.pos)                         #to not drag an empty square
                            dragger.drag_piece(piece)
                            game.show_bg(scr)
                            game.show_moves(scr)
                            game.show_pieces(scr)

                elif event.type == pygame.MOUSEMOTION:              #moving the mouse
                    motion_row = event.pos[1] // sqsize
                    motion_col = event.pos[0] // sqsize
                    game.set_hover(motion_row, motion_col)
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        game.show_bg(scr)
                        game.show_last_move(scr)
                        game.show_moves(scr)
                        game.show_pieces(scr)
                        dragger.update_blit(scr)
                
                elif event.type == pygame.MOUSEBUTTONUP:            #unclick event
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.Y // sqsize
                        released_col = dragger.X // sqsize

                        initial = Square(dragger.initial_row, dragger.initial_col)
                        final = Square(released_row, released_col)
                        move = Move(initial, final)

                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_col].has_piece()
                            board.move(dragger.piece, move)
                            board.set_true_en_passant(dragger.piece)
                            game.play_sound(captured)
                            game.show_bg(scr)
                            game.show_last_move(scr)
                            game.show_pieces(scr)
                            game.next_turn()       
                    dragger.undrag_piece()
                elif event.type == pygame.KEYDOWN:
                    if event.jey == pygame.K_t:
                        game.change_theme()
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger
                elif event.type == pygame.QUIT:                     #quit 
                    pygame.quit()
                    sys.exit()
            

            pygame.display.update()
        

main = Main()               # instances of the object
main.mainloop()
