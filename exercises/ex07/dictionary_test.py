"""EX07 - Dictionary Test Functions."""
__author__ = "730607229"


import pytest
from dictionary import invert, favorite_color, count


def test_invert_keyerror() -> None:
    """Test funtion invert with duplicated values in initial dictionary, raise a KeyError."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_empty_dictionary() -> None:
    """Test function invert with an empty dictionary."""
    dictionary: dict[str, str] = {}
    assert invert(dictionary) == {}


def test_invert_one_pair() -> None:
    """Test function invert with one key-value pair."""
    dictionary: dict[str, str] = {"one and only": "best friend"}
    assert invert(dictionary) == {"best friend": "one and only"}


def test_invert_multiple_pairs() -> None:
    """Test function invert with multiple key-value pairs."""
    dictionary: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(dictionary) == {"z": "a", "y": "b", "x": "c"}


def test_invert_multiple_pairs_again() -> None:
    """Test function invert with multiple key-value pairs again."""
    dictionary: dict[str, str] = {"money": "monkey", "CocaCola": "Sprite", "Pepsi": "Mtn Dew", "dog": "cheems", "cat": "buluga"}
    assert invert(dictionary) == {"monkey": "money", "Sprite": "CocaCola", "Mtn Dew": "Pepsi", "cheems": "dog", "buluga": "cat"}


def test_count_list_empty() -> None:
    """Test function count with empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_list_one_item_once() -> None:
    """Test function count with only one item occurs once in the list."""
    xs: list[str] = ["doge"]
    assert count(xs) == {"doge": 1}


def test_count_list_one_item_multiple_times() -> None:
    """Test function count with only one item occurs multiple times in the list."""
    xs: list[str] = ["love Suguru", "love Suguru", "love Suguru", "love Suguru", "love Suguru"]
    assert count(xs) == {"love Suguru": 5}


def test_count_list_multiple_item_once() -> None:
    """Test function count with multiple items occur only once in the list."""
    xs: list[str] = ["doge", "cheems", "buluga", "hecker"]
    assert count(xs) == {"doge": 1, "cheems": 1, "buluga": 1, "hecker": 1}


def test_count_list_multiple_item_multiple_times() -> None:
    """Test function count with multiple items occur multiple times in the list."""
    xs: list[str] = ["monkey", "money", "Satoru", "money", "monkey", "curse", "curse", "monkey", "money", "monkey", "monkey"]
    assert count(xs) == {"monkey": 5, "Satoru": 1, "money": 3, "curse": 2}


def test_favorite_color_empty() -> None:
    """Test function favorite_color with empty colors dictionary."""
    dictionary: dict[str, str] = {}
    assert favorite_color(dictionary) == ""


def test_favorite_color_one_item() -> None:
    """Test function favorite_color with one item in dictionary."""
    dictionary: dict[str, str] = {"Karmen": "blue"}
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_multiple_item_same_color() -> None:
    """Test function favorite_color with multiple people love the same color in dictionary."""
    dictionary: dict[str, str] = {"Karmen": "blue", "Coco": "blue", "Olivia": "blue"}
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_multiple_item_multiple_color() -> None:
    """Test function favorite_color with mutiple people love different colors in dictionary."""
    dictionary: dict[str, str] = {"Karmen": "blue", "Evelina": "pink", "Hua": "white", "Coco": "blue", "Olivia": "blue"}
    assert favorite_color(dictionary) == "blue"


def test_favorite_color_tie_colors() -> None:
    """Test function favorite_color with a tie for most popular color in dictionary."""
    dictionary: dict[str, str] = {"Karmen": "blue", "Evelina": "pink", "Lydia": "pink", "Hua": "white", "Coco": "blue", "Olivia": "blue"}
    assert favorite_color(dictionary) == "blue"
