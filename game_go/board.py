from game_go.group import Group
from game_go.my_enums import PionColor
from game_go.pion import Pion


class Board:

    def __init__(self, size):
        '''creating 2dlist of Pions which are classes'''
        self.__size = size
        self.__coordinates = [[Pion() for i in range(self.__size+2)]
                              for j in range(self.__size+2)]
        self.__create_edges()
        self.__group_dict = {}
        self.__uniq_id = 0
        

    def get_board_size(self):
        '''return horizonal and vertical size of board with edges'''
        return len(self.__coordinates), len(self.__coordinates[0])

    @property
    def coordinates(self):
        '''return coordinates[y][x]'''
        return self.__coordinates

    @property
    def group_dict(self):
        return self.__group_dict

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

    def get_field_color(self, x_coord: int, y_coord: int) -> PionColor:
        '''get color of field with coord x_coord and y_coord'''
        return self.__coordinates[y_coord][x_coord].pion_color


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
        self.__group_dict[self.__uniq_id] = Group(self.__uniq_id)
        self.__group_dict[self.__uniq_id].add_pion_to_group(x_coord, y_coord)
        self.__coordinates[y_coord][x_coord].group_id = self.__uniq_id
        self.__uniq_id += 1

    def remove_group_from_board(self, id: int):
        '''erase pions in group, and remove group'''
        print("halo")
        print(id)
        print(self.__group_dict[id].pions_list)

        for pion_coord in self.__group_dict[id].pions_list:
            self.__coordinates[pion_coord[1]][pion_coord[0]].erase_pion()
        # self.__group_dict.pop[id]
        del (self.__group_dict[id])

    def __assingn_pion_to_group(self, x_coord: int, y_coord: int):
        '''assingn pion to group'''
        self.create_new_group(x_coord, y_coord)

        if self.__coordinates[y_coord-1][x_coord].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.merge_groups(self.__group_dict[self.__coordinates[y_coord-1][x_coord].group_id],
                              self.__group_dict[self.__coordinates[y_coord][x_coord].group_id], self.__coordinates[y_coord][x_coord].group_id)
        if self.__coordinates[y_coord+1][x_coord].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.merge_groups(self.__group_dict[self.__coordinates[y_coord+1][x_coord].group_id],
                              self.__group_dict[self.__coordinates[y_coord][x_coord].group_id], self.__coordinates[y_coord][x_coord].group_id)
        if self.__coordinates[y_coord][x_coord-1].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.merge_groups(self.__group_dict[self.__coordinates[y_coord][x_coord-1].group_id],
                              self.__group_dict[self.__coordinates[y_coord][x_coord].group_id], self.__coordinates[y_coord][x_coord].group_id)
        if self.__coordinates[y_coord][x_coord+1].pion_color == self.__coordinates[y_coord][x_coord].pion_color:
            self.merge_groups(self.__group_dict[self.__coordinates[y_coord][x_coord+1].group_id],
                              self.__group_dict[self.__coordinates[y_coord][x_coord].group_id], self.__coordinates[y_coord][x_coord].group_id)

        self.__update_breath(x_coord, y_coord, self.__group_dict[self.__coordinates[y_coord][x_coord].group_id])

    def merge_groups(self, group_a: Group, group_b: Group, group_b_id: int):
        if group_a == group_b:
            return
        group_a.merge_pions_list(group_b)
        for x, y in group_b.pions_list:
            self.__coordinates[y][x].group_id = group_a.group_id
        del (self.__group_dict[group_b_id])

    def __update_breath(self, x_coord: int, y_coord: int, group: Group):
        '''update breath after setting pion in own group and affected group '''
        # update breath in own group
        breath = 0
        for x, y in group.pions_list:
            if self.__coordinates[y][x - 1].pion_color == PionColor.EMPTY:
                breath += 1
            if self.__coordinates[y][x + 1].pion_color == PionColor.EMPTY:
                breath += 1
            if self.__coordinates[y - 1][x].pion_color == PionColor.EMPTY:
                breath += 1
            if self.__coordinates[y + 1][x].pion_color == PionColor.EMPTY:
                breath += 1
        group.breath = breath
        # update breath in affected groups
        affected_group = []
        if self.__coordinates[y_coord][x_coord-1].pion_color == self.__coordinates[y_coord][x_coord].get_reversed_color():
            self.__group_dict[self.__coordinates[y_coord][x_coord-1].group_id].decrement_breath()
            if self.__group_dict[self.__coordinates[y_coord][x_coord-1].group_id].breath == 0:
                self.remove_group_from_board(self.__group_dict[self.__coordinates[y_coord][x_coord-1].group_id].group_id)



        if self.__coordinates[y_coord][x_coord + 1].pion_color == self.__coordinates[y_coord][
            x_coord].get_reversed_color():
            self.__group_dict[self.__coordinates[y_coord][x_coord + 1].group_id].decrement_breath()
            if self.__group_dict[self.__coordinates[y_coord][x_coord + 1].group_id].breath == 0:
                self.remove_group_from_board(self.__group_dict[self.__coordinates[y_coord][x_coord + 1].group_id].group_id)

        if self.__coordinates[y_coord - 1][x_coord].pion_color == self.__coordinates[y_coord][
            x_coord].get_reversed_color():
            self.__group_dict[self.__coordinates[y_coord - 1][x_coord].group_id].decrement_breath()
            if self.__group_dict[self.__coordinates[y_coord - 1][x_coord].group_id].breath == 0:
                self.remove_group_from_board(self.__group_dict[self.__coordinates[y_coord - 1][x_coord].group_id].group_id)

        if self.__coordinates[y_coord + 1][x_coord].pion_color == self.__coordinates[y_coord][
            x_coord].get_reversed_color():
            self.__group_dict[self.__coordinates[y_coord + 1][x_coord].group_id].decrement_breath()
            if self.__group_dict[self.__coordinates[y_coord + 1][x_coord].group_id].breath == 0:
                self.remove_group_from_board(self.__group_dict[self.__coordinates[y_coord + 1][x_coord].group_id].group_id)
