
class Group:

    def __init__(self, id):
        self.__pions_list = []
        self.__breath = None
        self.__id = id

    @property
    def breath(self):
        return self.__breath

    @breath.setter
    def breath(self, breath):
        if breath < 0:
            raise ValueError("group_id have to be greater equal 0")
        else:
            self.__breath = breath

    @property
    def pions_lists(self):
        return self.__pions_list

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

    def __update_pions_id(self, new_id: int):
        for pion in self.__pions_list:
            pion.group_id = new_id

    def remove_group(self):
        pass

    def __update_breath(self):
        pass

