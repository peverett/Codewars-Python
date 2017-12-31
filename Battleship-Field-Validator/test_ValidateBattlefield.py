#!/usr/bin/python

from ValidateBattlefield import validateBattlefield

class TestValidateBattlefield(object):

    def test_correct(battlefield):
        "A correct battleFIeld is valid"
        battleField =   [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                         [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        assert validateBattlefield(battleField) == True

    def test_no_ships(battlefield):
        "A battlefield with no ships"
        battleField =   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        assert validateBattlefield(battleField) == False

    def test_last_sub_missing(battlefield):
        "Valid but for 1 missing sub"
        battleField =   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]]

        assert validateBattlefield(battleField) == False

    def test_too_close_x(battlefield):
        "Ship too close on X column"
        battleField =   [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                         [1, 1, 1, 0, 0, 0, 0, 0, 1, 0],
                         [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        assert validateBattlefield(battleField) == False

    def test_too_close_y(battlefield):
        "Ship too close on Y column"
        battleField =   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]]

        assert validateBattlefield(battleField) == False

    def test_too_close_diagonal(battlefield):
        "Ship too close on diagonal"
        battleField =   [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 1, 1, 1, 0, 1, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                         [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]]

        assert validateBattlefield(battleField) == False

    def test_correct_on_edges(battlefield):
        "A correct battleFIeld is valid - all ships on edges"
        battleField =   [[1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                         [1, 0, 0, 0, 1, 1, 1, 0, 0, 1]]

#Test.assert_equals(validateBattlefield(battleField), True, "Yep! Seems alright", "Nope, something is wrong!");
