import pytest
from main import remove_space




@pytest.mark.parametrize("text, expected", [
    ("  abc ", "abc"),
    ("  abc", "abc"),
    ("abc  ", "abc"),
    (" ", ""),
])
def test_remove_space(text, expected):
    assert remove_space(text) == expected


def test_remove_space_is_not_none():
    assert remove_space("abc") is not None


@pytest.mark.parametrize("text", [
    "  hello  ",
    "  test",
    "example  ",
])
def test_remove_space_not_new_string(text):
    assert remove_space(text) == text.strip()


def test_remove_space_arguments():
    with pytest.raises(TypeError):
        remove_space()
