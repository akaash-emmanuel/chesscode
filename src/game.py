#this is to render the game, the board, the pieces 

import pygame

from constant import *
from board import Board
from dragger import Dragger
from config import Config
from square import Square

class Game:

    def __init__(self):
        self.next_player = 'white'
        self.hovered_sqr = None
        self.board = Board()
        self.dragger = Dragger()
        self.config = Config()

    def show_bg(self, surface):
        theme = self.config.theme

        for row in range(rows):
            for col in range(cols):
                color = theme.bg.light if (row + col) % 2 == 0 else theme.bg.dark
                rect = (col * sqsize, row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rect)

                if col == 0:
                    color = theme.bg.dark if row % 2 == 0 else theme.bg.light
                    label = self.config.font.render(str(rows-row), 1, color)
                    label_pos = (5, 5 + row * sqsize)
                    surface.blit(label, label_pos)

                if row == 7:
                    color = theme.bg.dark if (row + col) % 2 == 0 else theme.bg.light
                    label = self.config.font.render(Square.get_alphacol(col), 1, color)
                    label_pos = (col * sqsize + sqsize - 20, height - 20)
                    surface.blit(label, label_pos)

    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                if self.board.squares[row][col].has_piece():            #checking if we have a piece on a specific square
                    piece = self.board.squares[row][col].piece          #saving piece into variable

                    if piece is not self.dragger.piece:                #to render the piece except the dragging piece (remove duplicacy)
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)              #taking texture into image
                        img_center = col * sqsize + sqsize // 2, row * sqsize + sqsize // 2             #creating image center
                        piece.texture_rect = img.get_rect(center = img_center)    #center image on the square
                        surface.blit(img, piece.texture_rect)               #blit is a pregiven function to add image on square from variables
 
    def show_moves(self, surface):                                      #to make sure the valid moves are shown onky for the dragging piece
        theme = self.config.theme
        
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                rect = (move.final.col * sqsize, move.final.row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rect)

    
    def show_last_move(self, surface):
        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                rect = (pos.col * sqsize, pos.row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rect)

    def show_hover(self, surface):
        if self.hovered_sqr:
            color = (180, 180, 180)
            rect = (self.hovered_sqr.col * sqsize, self.hovered_sqr.row * sqsize, sqsize, sqsize)
            pygame.draw.rect(surface, color, rect, width=3)


    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self, row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme(self):
        self.config.change_theme()

    def play_sound(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()
    def reset(self):
        self.__init__()
    

