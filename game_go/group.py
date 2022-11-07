
class Group:

    def __init__(self, group_id):
        self.__pions_list = []
        self.__breath = None
        self.__group_id = group_id

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
    def pions_list(self):
        return self.__pions_list

    @pions_list.setter
    def pions_list(self, new_pion_list):
        self.__pions_list = new_pion_list
    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, group_id):
        if group_id < 0:
            raise ValueError("group_id have to be greater equal 0")
        else:
            self.__group_id = group_id

    def add_pion_to_group(self, x_coord, y_coord):
        '''add to __pion_list tuple of coordinates (x, y)'''
        self.__pions_list.append((x_coord, y_coord))

    def merge_pions_list(self, group: 'Group'):
        self.pions_list += group.pions_list

    def __update_pions_id(self, new_id: int):
        for pion in self.__pions_list:
            pion.group_id = new_id

    def decrement_breath(self):
        if self.__breath > 0:
            self.__breath-=1

