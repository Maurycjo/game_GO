import pytest
from game_go.board import Board
from game_go.my_enums import PionColor

def test_create_new_group_with_single_pion():
    board = Board(9)
    board.set_field(1, 1, PionColor.WHITE)
    board.set_field(1, 2, PionColor.BLACK)
    board.set_field(4, 4, PionColor.BLACK)
    board.set_field(6, 6, PionColor.WHITE)

    assert len(board.group_dict) == 4
    assert board.coordinates[1][1].group_id == 0
    assert board.coordinates[2][1].group_id == 1
    assert board.coordinates[4][4].group_id == 2
    assert board.coordinates[6][6].group_id == 3


def test_assigned_to_group():
    board = Board(9)
    board.set_field(1, 1, PionColor.WHITE)
    board.set_field(1, 2, PionColor.WHITE)
    assert board.coordinates[1][1].group_id == 0
    assert board.coordinates[2][1].group_id == 0
    assert len(board.group_dict[0].pions_list)== 2


    board.set_field(1, 4, PionColor.WHITE)
    assert board.coordinates[4][1].group_id == 2
    board.set_field(1, 3, PionColor.WHITE)
    assert len(board.group_dict[2].pions_list) == 4
    assert board.coordinates[1][1].group_id == 2
    assert board.coordinates[2][1].group_id == 2
    assert board.coordinates[4][1].group_id == 2
    assert board.coordinates[3][1].group_id == 2

def test_assigned_to_group_2():
    board = Board(9)
    board.set_field(1, 1, PionColor.WHITE)
    board.set_field(1, 2, PionColor.WHITE)
    assert board.coordinates[1][1].group_id == 0
    assert board.coordinates[2][1].group_id == 0
    assert len(board.group_dict[0].pions_list)== 2

    board.set_field(1, 4, PionColor.WHITE)
    assert board.coordinates[4][1].group_id == 2
    board.set_field(1, 3, PionColor.BLACK)

    assert board.coordinates[2][1].group_id == 0
    assert board.coordinates[4][1].group_id == 2
    assert board.coordinates[3][1].group_id == 3


def test_simple_breath_is_correct():
    board = Board(9)
    board.set_field(1, 1, PionColor.WHITE)
    assert board.group_dict[0].breath == 2

    board.set_field(1, 2, PionColor.WHITE)
    assert board.group_dict[0].breath == 3

    board.set_field(2, 1, PionColor.BLACK)
    assert board.group_dict[0].breath == 2
    assert board.group_dict[2].breath == 2

def test_update_breath():
    board = Board(9)
    board.set_field(3, 3, PionColor.WHITE)
    board.set_field(5, 3, PionColor.WHITE)
    board.set_field(4, 2, PionColor.WHITE)
    board.set_field(4, 4, PionColor.WHITE)
    board.set_field(4, 3, PionColor.WHITE)

    assert len(board.group_dict[board.coordinates[3][4].group_id].pions_list) == 5
    assert board.group_dict[board.coordinates[2][4].group_id].breath == 12




