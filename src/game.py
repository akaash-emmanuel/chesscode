#this is to render the game, the board, the pieces 

import pygame
from constant import *
from board import Board

class Game:
    def __init__(self):
        self.board = Board()

    def show_bg(self, surface):
        for row in range(rows):
            for col in range(cols):
                if (row + col) % 2 == 0:
                    color = (0, 0, 0)     #black
                else: 
                    color = (255, 255, 255)       #white

                rectangle = (col * sqsize, row * sqsize, sqsize, sqsize)
                pygame.draw.rect(surface, color, rectangle)
    
    def show_pieces(self, surface):
        for row in range(rows):
            for col in range(cols):
                if self.board.squares[row][col].has_piece():            #checking if we have a piece on a specific square
                    piece = self.board.squares[row][col].piece          #saving piece into variable

                    img = pygame.image.load(piece.texture)              #taking texture into image
                    img_center = col * sqsize + sqsize // 2, row * sqsize + sqsize // 2             #creating image center
                    piece.texture_rect = img.get_rect(center = img_center)    #center image on the square
                    surface.blit(img, piece.texture_rect)               #blit is a pregiven function to add image on square from variables
