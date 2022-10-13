from my_enums import PionColor


class Pion:

    def __init__(self):
        self.__pion_color = PionColor.EMPTY

    @property
    def pion_color(self):
        return self.__pion_color

    @pion_color.setter
    def pion_color(self, color: PionColor):
        self.__pion_color = color

    def get_pion_symbol(self):
        '''Return pion symbol for empty(" "), for black (x), for white (o)'''
        if self.__pion_color == PionColor.EMPTY:
            return "-"
        if self.__pion_color == PionColor.BLACK:
            return "x"
        if self.__pion_color == PionColor.WHITE:
            return "o"