import pytest

from game_go.board import Board
from game_go.my_enums import PionColor

def test_can_create_board():
    board = Board(9)
    assert board is not None


def test_size_of_board_with_edges():
    board = Board(4)
    size_x, size_y = board.get_board_size()
    assert size_x == 6 and size_y ==6

def test_if_egde_create_correct():
    '''check if edge create correct'''
    board = Board(9)
    correct = True
    for i in range(9):
        assert board.get_field_color(i, 0) == PionColor.EDGE
        assert board.get_field_color(i, 10) == PionColor.EDGE
        assert board.get_field_color(0, i) == PionColor.EDGE
        assert board.get_field_color(10, i) == PionColor.EDGE

def test_put_pion_on_board():
    board = Board(9)
    board.set_field(1, 1, PionColor.BLACK)
    board.set_field(3, 4, PionColor.BLACK)
    board.set_field(4, 3, PionColor.WHITE)
    board.set_field(2, 8, PionColor.WHITE)

    assert board.get_field_color(1, 1) == PionColor.BLACK
    assert board.get_field_color(3, 4) == PionColor.BLACK
    assert board.get_field_color(4, 3) == PionColor.WHITE
    assert board.get_field_color(2, 8) == PionColor.WHITE


def test_put_pion_on_board_expected_index_error():
    board = Board(9)

    with pytest.raises(IndexError):
        board.set_field(-1,0, PionColor.WHITE)
    with pytest.raises(IndexError):
        board.set_field(-2,-2, PionColor.BLACK)
    with pytest.raises(IndexError):
        board.set_field(4,-3, PionColor.WHITE)
    with pytest.raises(IndexError):
        board.set_field(1,12, PionColor.BLACK)
    with pytest.raises(IndexError):
        board.set_field(12, 1, PionColor.WHITE)
    with pytest.raises(IndexError):
        board.set_field(0, 0, PionColor.BLACK)
    with pytest.raises(IndexError):
        board.set_field(9, 10, PionColor.BLACK)


def test_put_pion_on_board_expected_value_error():
    board = Board(9)
    board.set_field(2, 1, PionColor.BLACK)
    board.set_field(1, 2, PionColor.BLACK)
    board.set_field(3, 2, PionColor.WHITE)
    board.set_field(3, 4, PionColor.WHITE)
    board.set_field(2, 3, PionColor.WHITE)
    board.set_field(4, 3, PionColor.WHITE)
    #overwriting
    with pytest.raises(ValueError):
        board.set_field(3, 2, PionColor.WHITE)
    with pytest.raises(ValueError):
        board.set_field(3, 2, PionColor.BLACK)
    with pytest.raises(ValueError):
        board.set_field(2, 1, PionColor.BLACK)
    with pytest.raises(ValueError):
        board.set_field(4, 3, PionColor.BLACK)
    #suicide move
    with pytest.raises(ValueError):
        board.set_field(3, 3, PionColor.BLACK)
    with pytest.raises(ValueError):
        board.set_field(1, 1, PionColor.WHITE)

