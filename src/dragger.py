import pygame
from constant import *


class Dragger:

    def __init__(self):
        self.X = 0
        self.Y = 0
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.dragging = False

    def update_blit(self, surface):         #updating the piece visually when dragged
        self.piece.set_texture(size=128)    #make dragging piece bigger visually
        texture = self.piece.texture

        img = pygame.image.load(texture)   #image
        img_center = (self.X, self.Y)
        
        self.piece.texture_rect = img.get_rect(center=img_center)  #centering the image on the square
        surface.blit(img, self.piece.texture_rect)   #rendering the image


    def update_mouse(self, pos):
        self.X, self.Y = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // sqsize
        self.initial_col = pos[0] // sqsize

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
    