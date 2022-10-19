from pion import Pion
from itertools import groupby


class Group:

    def __init__(self):
        self.__pions_list = []
        self.__breath = None
        self.__id = -1

    @property
    def breath(self):
        return self.__breath

    @property
    def pions_lists(self):
        return self.__pions_list

    @pions_lists.setter
    def pions_lists(self, list):
        return list

    @property
    def id(self):
        return self.__id

    @id.setter
    def group_id(self, id):
        if id < 0:
            raise ValueError("group_id have to be greater equal 0")
        else:
            self.__id = id

    def add_pion_to_group(self, x_coord, y_coord):
        '''add to __pion_list tuple of coordinates (x, y)'''
        self.__pions_list.append((x_coord, y_coord))
        self.__update_breath()

    def merge_pions_list(self, group: 'Group'):
        self.pions_lists += group.pions_lists

    def remove_group(self):
        pass

    def __update_breath(self):
        pass


if __name__ == "__main__":
    lista = [0, 1, 2]
    lista2 = [3, 5, 6]
    lista += lista2
    print(lista)
