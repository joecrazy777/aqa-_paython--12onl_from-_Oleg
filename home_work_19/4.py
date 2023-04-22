from main import fields
import pytest


def test_example_values_1():
    assert fields(10, 10) == 6

def test_example_values_2():
    assert fields(100, 10) == 12

def test_example_values_3():
    assert fields(1000, 10) == 18

def test_small_initial_difference():
    assert fields(10, 1) == 12

def test_s2_greater_than_s1():
    assert fields(5, 10) == 4