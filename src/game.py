#this is to render the game, the board, the pieces 

import pygame
from constant import *
from board import Board
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (181, 136, 99)     #black, have to change because of image colors (color taken from google reference)
                else: 
                    color = (241, 217, 180)       #white, same as above

                rectangle = (col * sqsize, row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rectangle)
    
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
        if self.dragger.dragging:
            piece = self.dragger.piece

            for move in piece.moves:
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'      #colors of the valid moves
                rect = (move.final.col * sqsize, move.final.row * sqsize, sqsize, sqsize)           #boundary of the color
                pygame.draw.rect(surface, color, rect)          #render to the game

