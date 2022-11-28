"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730607229"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_last_one_item() -> None:
    """Test last of a single item list return its own data value."""
    linked_list = Node(1, None)
    assert last(linked_list) == 1


def test_last_mutiple_items() -> None:
    """Test last of a mutiple items list return its last data value."""
    linked_list = Node(5, Node(10, Node(15, Node(20, Node(25, None)))))
    assert last(linked_list) == 25


def test_value_at_empty() -> None:
    """Value at of an empty Linked List should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)
    

def test_value_at_index_zero() -> None:
    """Value at index zero should return the data of the current Node being processed on the list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 0) == 1


def test_value_at_index_one() -> None:
    """Value at index one should return the data of the second Node being processed on the list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_value_at_index_two() -> None:
    """Value at index two should return the data of the third Node being processed on the list."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 2) == 3


def test_max_empty() -> None:
    """Max of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_max_single() -> None:
    """Max of a Linked List with a single item should return the data value of it."""
    linked_list = Node(10, None)
    assert max(linked_list) == 10


def test_max_maximum_data_last() -> None:
    """Max of an Linked List with the maximum data in the end should return the last one."""
    linked_list = Node(10, Node(20, Node(30, None)))
    assert max(linked_list) == 30


def test_max_maximum_data_middle() -> None:
    """Max of an Linked List with the maximum data in the middle should return the one in the middle."""
    linked_list = Node(10, Node(20, Node(30, Node(20, Node(10, None)))))
    assert max(linked_list) == 30


def test_max_maximum_data_first() -> None:
    """Max of an Linked List with the maximum data on the first should return the first one."""
    linked_list = Node(30, Node(20, Node(10, None)))
    assert max(linked_list) == 30


def test_max_maximum_data_different_order() -> None:
    """Max of an Linked List with the maximum data on the first should return the first one."""
    linked_list = Node(30, Node(20, Node(10, Node(40, None))))
    assert max(linked_list) == 40


def test_linkify_empty_list() -> None:
    """Linkify of an empty list should return None."""
    items: list[int] = []
    assert linkify(items) is None


def test_linkify_list_one_item() -> None:
    """Linkify of a list of one item."""
    items: list[int] = [10]
    assert str(linkify(items)) == "10 -> None"


def test_linkify_list_multiple_items() -> None:
    """Linkify of a list of multiple items."""
    items: list[int] = [5, 7, 2]
    assert str(linkify(items)) == "5 -> 7 -> 2 -> None"


def test_linkify_list_multiple_items_again() -> None:
    """Linkify of a list of multiple items again."""
    items: list[int] = [3, 3, 7, 7, 10]
    assert str(linkify(items)) == "3 -> 3 -> 7 -> 7 -> 10 -> None"


def test_scale_empty() -> None:
    """Scale of an empty Linked List should return None."""
    assert scale(None, 1) is None


def test_scale_one_item() -> None:
    """Scale of a Linked List should return a new linked list with the original value scale by the factor parameter."""
    linked_list = Node(10, None)
    assert str(scale(linked_list, 5)) == "50 -> None"


def test_scale_multiple_items() -> None:
    """Scale of a Linked List should return a new linked list with the original value scale by the factor parameter."""
    linked_list = linkify([1, 2, 3])
    assert str(scale(linked_list, 2)) == "2 -> 4 -> 6 -> None"


def test_scale_multiple_items_again() -> None:
    """Scale of a Linked List should return a new linked list with the original value scale by the factor parameter."""
    linked_list = linkify([10, 20, 30, 40, 50])
    assert str(scale(linked_list, 2)) == "20 -> 40 -> 60 -> 80 -> 100 -> None"
