from game_go.board import Board


def test_can_create_board():
    board = Board(9)
    assert board != None
