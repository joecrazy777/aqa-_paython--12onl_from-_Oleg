from main import area_calculation
import pytest


class TestArea:
    def test_one(self):
        s_one, s_two, year = area_calculation(1, 5)
        assert s_one == 4
        assert s_two == 45
        assert year == 3

    def test_two(self):
        result = area_calculation(None, 5)
        assert result == "Error"


# def test_area_calculation():

    # assert area_calculation(2, 3) == (64, 729, 6)
    # assert area_calculation(10, 15) == (320, 3645, 6)
    # assert area_calculation(1, 1) == (64, 729, 7)
    #
    #
    # assert area_calculation(2.5, 3) == "Error"
    # assert area_calculation(2, "3") == "Error"
    #
    #
    # assert area_calculation(1, 2) == (16, 162, 5)