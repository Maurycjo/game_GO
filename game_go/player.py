from my_enums import PionColor

class Player:

    def select_name(self):
        self.player_name = input("Enter your name: ")

    def choose_color(self):
        symbol = input("What symbol you want: 'o' or 'x': ")
        while symbol != 'o' and symbol != 'x':
            symbol = input("Please chose correct symbol: ")

        if symbol =='o':
            self.player_color = PionColor.WHITE
        else:
            self.player_color = PionColor.BLACK

    def get_reversed_color(self):
        if self.symbol =='o':
            return 'x'
        return 'o'

