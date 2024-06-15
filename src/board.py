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
                (row-2, col+1),
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
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):        # if the valid square is empty, its possible, otherwise it isnt
                        
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        move = Move(initial, final)
                        piece.add_move(move)

        def pawn_moves():
            steps = 1 if piece.moved else 2

            # vertical moves
            start = row + piece.dir  
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)

                        move = Move(initial, final)
                        piece.add_move(move)
                    else:
                        break                   #pawn stops when square is occupied
                else:
                    break           #not in range and breaks the loop

                #diagonal eliminations
                possible_move_row = row + piece.dir
                possible_move_cols = [col-1, col+1]
                for possible_move_col in possible_move_cols:
                    if Square.in_range(possible_move_row, possible_move_col):
                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            initial = Square(row, col)
                            final = Square(possible_move_row, possible_move_col)
                            move = Move(initial, final)
                            piece.add_move(move)

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)

                        if self.squares[possible_move_row][possible_move_col].isempty():
                            piece.add_move(move)

                        if self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            piece.add_move(move)
                            break

                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break        
                        
                    else: break

                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            adjs = [
                 (row-1, col+0)
                 (row-1, col+1)       
                 (row+0, col+1)       
                 (row+1, col+1)       
                 (row+1, col+0)       
                 (row+1, col-1)       
                 (row+0, col-1)       
                 (row-1, col-1)       
            ]
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_move(move)
            
        if isinstance(piece, Pawn):
            pawn_moves()
        elif isinstance(piece, Knight):
            knight_moves()
        elif isinstance(piece, Bishop):
            straightline_moves([
                (-1,1),
                (-1,-1),
                (1,1),
                (1,-1)
            ])
        elif isinstance(piece, Rook):
            straightline_moves([
                (-1,0),
                (0,1),
                (1,0),
                (0,-1)
            ])
        elif isinstance(piece, Queen):
            straightline_moves([
                (-1,1),
                (-1,-1),
                (1,1),
                (1,-1),
                (-1,0),
                (0,1),
                (1,0),
                (0,-1)
            ])
        elif piece.name == 'king':
            king_moves()

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

