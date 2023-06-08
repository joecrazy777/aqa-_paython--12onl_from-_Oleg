import pytest
from main import numms


@pytest.mark.parametrize("a,b,expected", [(2, 10, 54), (3, 12, 75), (4, 19, 184)])
def test_numms(a, b, expected):
    assert numms(a, b) == expected


@pytest.mark.parametrize("a,b,Error", [(25, 5, "Error"),
                                       (10.0, 5, "Error"),
                                       (10, 5.0, "Error"),
                                       (2.2, 5, "Error"),
                                       (2, 5.5, "Error")])
def test_numms_type(a, b):
    with pytest.raises(TypeError):
        numms(a, b)
