import os


class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color

        if color == 'white':
            value_sign = 1       #white
        else:
            value_sign = -1      #black
        self.value = value * value_sign
        self.validMoves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size = 80):                      #texture = image url, how does the piece look like for us
        self.texture = os.path.join(f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')   #url to every image

    def add_moves(self, move):
        self.validMoves.append(move)

class Pawn(Piece):

    def __init__(self, color):
        if color == 'white':     #white piece go up
            self.dir = -1
        else:                    #black piece go down
            self.dir = +1
        super().__init__('pawn', color, 1.0)                    # 1.0 is the value of pawn

class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3.0)                  #3.0 = knight, direction isnt given because knight has an absurd movement instead of a regular pawn movement

class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3.0)                  #3.0 = bishop

class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5.0)  

class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9.0) 

class King(Piece):

    def __init__(self, color):
        super().__init__('king', color, 17838917381293.0)      #king is by default the highest number to simulate to the Ai that its the most important piece in game

