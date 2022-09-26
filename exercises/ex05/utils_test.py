"""EX05 - `list` Utility Test Functions."""
__author__ = "730607229"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Test function only_even for an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_all_even() -> None:
    """Test function only_even for a list with all even numbers."""
    xs: list[int] = [2, 4, 6]
    assert only_evens(xs) == [2, 4, 6]


def test_only_evens_all_odd() -> None:
    """Test function only_even for a list with all odd numbers."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_only_evens_many_numbers() -> None:
    """Test function only_even for a list with many numbers."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_concat_empty() -> None:
    """Test function concat with two empty lists."""
    xs_a: list[int] = []
    xs_b: list[int] = []
    assert concat(xs_a, xs_b) == []


def test_concat_one_empty() -> None:
    """Test function concat with two empty lists."""
    xs_a: list[int] = [5]
    xs_b: list[int] = []
    assert concat(xs_a, xs_b) == [5]


def test_concat_list_length_same() -> None:
    """Test function concat with two lists with same length."""
    xs_a: list[int] = [1, 2, 0, 7]
    xs_b: list[int] = [0, 2, 0, 3]
    assert concat(xs_a, xs_b) == [1, 2, 0, 7, 0, 2, 0, 3]


def test_concat_list_length_different() -> None:
    """Test function concat with two lists with different length."""
    xs_a: list[int] = [5]
    xs_b: list[int] = [7, 2]
    assert concat(xs_a, xs_b) == [5, 7, 2]


def test_concat_many_items() -> None:
    """Test function concat with many items in the two lists."""
    xs_a: list[int] = [-99, 0]
    xs_b: list[int] = [0, 99]
    assert concat(xs_a, xs_b) == [-99, 0, 0, 99]


def test_sub_list_empty() -> None:
    """Test function sub with an empty list, start is greater than the length of the list."""
    xs: list[int] = []
    assert sub(xs, 1, 5) == []


def test_sub_end_at_most_zero() -> None:
    """Test function sub with end at most zero."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 0) == []


def test_sub_start_negative() -> None:
    """Test function sub with start negative, start from the beginning of the list."""
    xs: list[int] = [12, 7, 2, 3]
    assert sub(xs, -10, 2) == [12, 7]


def test_sub_end_greater_length_list() -> None:
    """Test function sub with end index is greater than the length of the list, end with the end of the list."""
    xs: list[int] = [12, 7, 2, 3]
    assert sub(xs, 0, 8) == [12, 7, 2, 3]


def test_sub_many_items() -> None:
    """Test function sub with many items in the list, begin with the start index and end with end index minus 1."""
    xs: list[int] = [10, 20, 30, 40]
    assert sub(xs, 1, 3) == [20, 30]


def test_sub_many_items_again() -> None:
    """Test function sub with many items in the list, begin with the start index and end with end index minus 1."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7]
    assert sub(xs, 2, 6) == [3, 4, 5, 6]
