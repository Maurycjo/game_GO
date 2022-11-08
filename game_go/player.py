from game_go.my_enums import PionColor

class Player:

    def __init__(self):
        self.__symbol = None
        self.__player_name = None

    @property
    def symbol(self):
        return self.__symbol

    @symbol.setter
    def symbol(self, new_symbol):
        if new_symbol == 'o' or new_symbol =='x':
            self.__symbol = new_symbol
        else:
            raise ValueError("Bad symbol, you can choose only 'o' or 'x'")

    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, new_player_name):
        self.__player_name = new_player_name

    def select_name_console(self):
        self.player_name = input("Enter your name: ")

    def choose_color_console(self):
        '''choose 'o' or 'x' while exception occurs'''
        while True:
            try:
                self.symbol = input("What symbol you want: 'o' or 'x': ")
            except ValueError as e:
                print(e)
            else:
                break

    def get_reversed_color(self):
        '''if it possible get reversed symbol'''
        if self.symbol == 'o':
            return 'x'
        if self.symbol == 'x':
            return 'o'
        return None


