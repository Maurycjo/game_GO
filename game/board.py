import numpy as np
from my_enums import PionColor
from pion import Pion


class Board:

    def __init__(self, size):
        self.__size = size
        self.__coordinates = [[Pion() for i in range(self.__size)]
                              for j in range(self.__size)]

    def display_board(self):
        print(" ", end="")
        for i in range(self.__size):
            print("", i, end="")
        print()
        for index, item in enumerate(self.__coordinates):
            print(index, end="")
            for pion in item:
                print(" " + pion.get_pion_symbol(), end="")
            print()

    def set_field(self, x_coord: int, y_coord: int, color: PionColor):
        self.__coordinates[y_coord][x_coord].pion_color = color


if __name__ == "__main__":
    board = Board(9)
    board.set_field(0, 2, PionColor.BLACK)
    board.display_board()
    board.set_field(1, 2, PionColor.WHITE)
    board.display_board()
