from ast import While
import numpy as np
from group import Group
from my_enums import PionColor
from pion import Pion


class Board:

    def __init__(self, size):
        '''creating 2dlist of Pions which are classes'''
        self.__size = size
        self.__coordinates = [[Pion() for i in range(self.__size+2)]
                              for j in range(self.__size+2)]
        self.__create_edges()
        self.__group_dict = {}
        self.__uniq_id = 0

    def __create_edges(self):
        '''create edges with specified properties on board'''
        for index, pion in enumerate(self.__coordinates[0]):
            pion.pion_color = PionColor.EDGE
            self.__coordinates[index][0].pion_color = PionColor.EDGE

        for index, pion in enumerate(self.__coordinates[self.__size+1]):
            pion.pion_color = PionColor.EDGE
            self.__coordinates[index][self.__size +
                                      1].pion_color = PionColor.EDGE

    def display_board(self):
        '''display board in console mode'''
        print("   ", end="")
        for i in range(1, self.__size+1):
            print("", i, end="")
        print()
        for index, item in enumerate(self.__coordinates):
            if index == 0 or index == self.__size+1:
                print(" ", end="")
            else:
                print(index, end="")
            for pion in item:
                print(" " + pion.get_pion_symbol(), end="")
            print()

    def set_field(self, x_coord: int, y_coord: int, color: PionColor):
        '''corection of valid data, and set field with certtain coordinations '''
        if x_coord < 1 or y_coord < 1 or x_coord > self.__size or y_coord > self.__size:
            raise IndexError(
                "Bad coordinates, coordinates must be beetwen <{min_val},{max_val}>".format(min_val=1, max_val=self.__size))
        elif self.__coordinates[y_coord][x_coord].pion_color != PionColor.EMPTY:
            raise ValueError("Bad coordinates, can't overwrite this field")
        elif self.__check_if_suicide_move(x_coord, y_coord, color):
            raise ValueError("Suicide move")
        else:
            self.__coordinates[y_coord][x_coord].pion_color = color
            self.__assingn_pion_to_group(x_coord, y_coord)

    def __check_if_suicide_move(self, x_coord: int, y_coord: int, color: PionColor):
        '''check if move is suicide, if suicide return True, else False'''
        breath = 4
        if self.__coordinates[y_coord-1][x_coord].pion_color == color or self.__coordinates[y_coord-1][x_coord].pion_color == PionColor.EMPTY:
            return False
        if self.__coordinates[y_coord+1][x_coord].pion_color == color or self.__coordinates[y_coord+1][x_coord].pion_color == PionColor.EMPTY:
            return False
        if self.__coordinates[y_coord][x_coord-1].pion_color == color or self.__coordinates[y_coord][x_coord-1].pion_color == PionColor.EMPTY:
            return False
        if self.__coordinates[y_coord][x_coord+1].pion_color == color or self.__coordinates[y_coord][x_coord+1].pion_color == PionColor.EMPTY:
            return False
        return True

    def create_new_group(self, x_coord: int, y_coord: int):
        '''create new group with unique id in dictionary'''
        self.__group_dict[self.__uniq_id] = Group()
        print("uniqID: ", self.__uniq_id)
        self.__group_dict[self.__uniq_id].add_pion_to_group(x_coord, y_coord)
        self.__coordinates[y_coord][x_coord].group_id = self.__uniq_id
        self.__uniq_id += 1

    def remove_group_from_board(self, id: int):
        '''erase pions in group, and remove group'''
        for pion_coord in self.__group_dict[id]:
            self.__coordinates[pion_coord[0]][pion_coord[1]].erase_pion()
        self.__group_dict.pop[id]

    def __pop_group(self):
        '''pop group when Pion immediately assignet to group'''
        pass

    def __assingn_pion_to_group(self, x_coord: int, y_coord: int):
        '''assingn pion to group'''
        # type_of_assign:
        #  0- new group
        #  1- to existing group,
        #  2- to existing group with merge 2 groups
        #  3- to existing group with merge 3 groups
        #  4- to existing group with merge 4 groups

        self.create_new_group(x_coord, y_coord)

        if self.__coordinates[y_coord-1][x_coord].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.__group_dict[self.__coordinates[y_coord-1]
                              [x_coord].group_id].merge_groups(self.__coordinates[y_coord][x_coord].group_id)
        if self.__coordinates[y_coord+1][x_coord].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.__group_dict[self.__coordinates[y_coord+1]
                              [x_coord].group_id].merge_groups(self.__coordinates[y_coord][x_coord].group_id)
        if self.__coordinates[y_coord][x_coord-1].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.__group_dict[self.__coordinates[y_coord]
                              [x_coord-1].group_id].merge_groups(self.__coordinates[y_coord][x_coord].group_id)
        if self.__coordinates[y_coord][x_coord+1].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.__group_dict[self.__coordinates[y_coord]
                              [x_coord+1].group_id].merge_groups(self.__coordinates[y_coord][x_coord].group_id)


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
