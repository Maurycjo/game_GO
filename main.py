from game_go.board import Board
from game_go.group import Group
from game_go.my_enums import PionColor
from game_go.pion import Pion
from game_go.player import Player


if __name__ =="__main":
    print("Welcome in Game Go")
    board_size = input("Please enter what board size you want: ")

    board = Board(board_size)
    player1 = Player()
    player2 = Player()
    player1.select_name()
    player2.select_name()
    player1.choose_color()
    player2.choose_color(player1)

    turn = 0

    while True:
            print("type 'exit' if you want leave")
            print(player1.player_name) if turn % 2 == 0 else print(player2.player_name)
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