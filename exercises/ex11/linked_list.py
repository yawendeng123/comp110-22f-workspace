"""Utility functions for working with Linked Lists."""

from __future__ import annotations
from typing import Optional

__author__ = "730607229"


class Node:
    """An item in a singly-linked list."""
    data: int
    next: Optional[Node]

    def __init__(self, data: int, next: Optional[Node]):
        """Construct a singly linked list. Use None for 2nd argument if tail."""
        self.data = data
        self.next = next

    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"


def is_equal(lhs: Optional[Node], rhs: Optional[Node]) -> bool:
    """Test if two linked lists are deeply (values and order) equal to one another."""
    if lhs is None and rhs is None:
        return True
    elif lhs is None or rhs is None or lhs.data != rhs.data:
        return False
    else:
        return is_equal(lhs.next, rhs.next)


def last(head: Optional[Node]) -> int:
    """Returns the last value of a Linked List, or raises a ValueError if the list is empty."""
    if head is None:
        raise ValueError("last cannot be called with None")
    else:
        if head.next is None:
            return head.data
        else:
            return last(head.next)


def value_at(head: Optional[Node], index: int) -> int:
    """Given a head Optional[Node] and an index int as inputs, return the data of the Node stored at the given index, or raise an IndexError if the index does not exist."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    else:
        if index == 0:
            return head.data
        else:
            return value_at(head.next, index - 1)


def max(head: Optional[Node]) -> int:
    """Given a head Node, return the maximum data value in the linked list. If the linked list is empty, raise a ValueError."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.data
    else:
        maximum = max(head.next)
        if head.data <= maximum:
            return maximum
        else:
            return head.data
        

def linkify(items: list[int]) -> Optional[Node]:
    """Given a list[int], return a Linked List of Nodes with the same values, in the same order, as the input list."""
    if items == []:
        return None
    else:
        n: Node = Node(items[0], None)
        if len(items) == 1:
            return n
        else:
            n.next = linkify(items[1:])
            return n


def scale(head: Optional[Node], factor: int) -> Optional[Node]:
    """Given a head Node of a linked list and a int factor to scale by, return a new linked list of Nodes where each value in the original list is scaled (multiplied) by the scaling factor."""
    if head is None:
        return None
    else:
        n: Node = Node(head.data * factor, None)
        if head.next is None:
            return n
        else:
            n.next = scale(head.next, factor)
            return n
