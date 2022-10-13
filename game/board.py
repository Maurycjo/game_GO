import numpy as np


class Board:

    def __init__(self, size):
        self.__size = size
        self.__coordinates = np.full((self.__size, self.__size,), "-")

    def display_board(self):
        print("  ", end="")
        for i in range(self.__size):
            print("", i, end="")
        print()
        for index, i in enumerate(self.__coordinates):
            print(index, " ", end="")
            print(" ".join(i))


if __name__ == "__main__":
    board = Board(9)
    board.display_board()
