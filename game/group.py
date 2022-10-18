from pion import Pion


class Group:

    def __init__(self):
        self.__pions_list = []
        self.__breath = None

    @property
    def breath(self):
        return self.__breath

    @property
    def pions_lists(self):
        return self.__pions_list

    def add_pion_to_group(self, x_coord, y_coord):
        '''add to __pion_list tuple of coordinates (x, y)'''
        self.__pions_list.append((x_coord, y_coord))
        self.__update_breath()

    def remove_group(self):
        pass

    def merge_groups(self, group: 'Group'):
        print("that methot didnt implemented yet")

    def __update_breath(self):
        pass


if __name__ == "__main__":
    pass
