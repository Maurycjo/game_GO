from my_enums import PionColor


class Pion:

    def __init__(self):
        '''initialization with empty Pion'''
        self.__pion_color = PionColor.EMPTY
        self.__group_id = -1

    @property
    def pion_color(self):
        '''get pion color'''
        return self.__pion_color

    @pion_color.setter
    def pion_color(self, color: PionColor):
        '''set pion color with enum PionColor'''
        self.__pion_color = color

    @property
    def group_id(self):
        return self.__group_id

    @group_id.setter
    def group_id(self, id):
        if id < 0:
            raise ValueError("group_id have to be greater equal 0")
        else:
            self.__group_id = id

    def erase_pion(self):
        self.__pion_color = PionColor.EMPTY
        self.__group_id = -1

    def get_pion_symbol(self):
        '''Return pion symbol for empty(" "), for black (x), for white (o)'''
        if self.__pion_color == PionColor.EMPTY:
            return "-"
        if self.__pion_color == PionColor.BLACK:
            return "x"
        if self.__pion_color == PionColor.WHITE:
            return "o"
        if self.__pion_color == PionColor.EDGE:
            return "#"
