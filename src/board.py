from constant import *
from square import Square
from piece import *
from move import Move

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(cols)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

# to calculate all valid moves of a piece on a position
    def calc_moves(self, piece, row, col):

        def knight_moves():
            possible_moves = [
                (row-2, col +1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row, possible_move_col].isempty_or_rival(piece.color):        # if the valid square is empty, its possible, otherwise it isnt
                        
                        initial =   Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        move = Move(initial, final)
                        piece.add_move(move)

        if piece.name == 'pawn':
            pass

        elif piece.name == 'knight':
            knight_moves()

        elif piece.name == 'bishop':
            pass

        elif piece.name == 'rook':
            pass

        elif piece.name == 'queen':
            pass

        elif piece.name == 'king':
            pass

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

