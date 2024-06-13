from constant import *
from square import Square

class Board:
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(cols)]
        self._create()

    def _create(self):  
        for row in range(rows):
            for col in range(cols):
                self.squares[row][col] = Square(row,col)

    def _add_pieces(self, color):
        pass