from game_go.board import Board
from game_go.my_enums import PionColor
from game_go.player import Player
import os

if __name__ =="__main__":
    print("Welcome in Game Go")
    board_size = int(input("Please enter what board size you want: "))

    board = Board(board_size)
    player1 = Player()
    player2 = Player()
    print("player1, ", end="")
    player1.select_name_console()
    player1.choose_color_console()

    print("player2, ", end="")
    player2.select_name_console()
    player2.symbol = player1.get_reversed_color()

    turn = 0

    while True:
            os.system('clear')
            board.display_board()
            print("type 'exit' to leave game")
            print(player1.player_name) if turn % 2 == 0 else print(player2.player_name)
            x = input("podaj x: ")
            if x == "exit":
                break
            y = input("podaj y: ")
            if y == "exit":
                break
            x = int(x)
            y = int(y)
            try:
                if turn % 2 == 0:
                    board.set_field(x, y, PionColor.BLACK)
                else:
                    board.set_field(x, y, PionColor.WHITE)
                turn += 1
            except IndexError as e:
                print(e)
            except ValueError as e:
                print(e)