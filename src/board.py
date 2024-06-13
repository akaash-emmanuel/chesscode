from constant import *
from square import Square
from piece import *

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(cols)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):  
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row,col)

    def _add_pieces(self, color):
        if color == 'white':
            row_pawn, row_other = (6,7)         #6 and 7 are row numbers (0,1,2,3,4,5,6,7), pawns are 6 and others are 7
        else:
            row_pawn, row_other = (1,0)         #black pieces initialized on board

        for col in range(cols):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))    #pawns are created on board
        
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))        #knight positions
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))        #knight positions

        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))        #bishop
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))        #bishop

        self.squares[row_other][0] = Square(row_other, 0, Rook(color))        #rook
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))        #rook

        self.squares[row_other][3] = Square(row_other, 3, Queen(color))         #queen

        self.squares[row_other][4] = Square(row_other, 4, King(color))          #king

