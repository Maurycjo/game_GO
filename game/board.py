import numpy as np
from pion import Pion


class Board:

    def __init__(self, size):
        self.__size = size
        self.__coordinates = np.full((self.__size, self.__size,), Pion())

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


if __name__ == "__main__":
    board = Board(9)
    board.display_board()
