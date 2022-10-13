from ast import While
import numpy as np
from my_enums import PionColor
from pion import Pion


class Board:

    def __init__(self, size):
        '''creating 2dlist of Pions which are classes'''
        self.__size = size
        self.__coordinates = [[Pion() for i in range(self.__size)]
                              for j in range(self.__size)]

    def display_board(self):
        '''display board in console mode'''
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
        '''corection of valid data, and set field with certtain coordinations '''
        if x_coord < 0 > y_coord or x_coord >= self.__size <= y_coord:
            raise IndexError(
                "Bad coordinates, coordinates must be beetwen <0,8>")
        elif self.__coordinates[y_coord][x_coord].pion_color != PionColor.EMPTY:
            raise ValueError("Bad coordinates, can't overwrite this field")
        self.__coordinates[y_coord][x_coord].pion_color = color


if __name__ == "__main__":
    board = Board(9)
    turn = 0

    while True:
        print("czarny") if turn % 2 == 0 else print("bialy")
        x = int(input("podaj x: "))
        if x == 420:
            break
        y = int(input("podaj y: "))
        try:
            if turn % 2 == 0:
                board.set_field(x, y, PionColor.BLACK)
                board.display_board()
            else:
                board.set_field(x, y, PionColor.WHITE)
                board.display_board()
            turn += 1
        except IndexError as e:
            print(e)
        except ValueError as e:
            print(e)
