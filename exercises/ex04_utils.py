"""EX04 - `list` Utility Functions."""
__author__ = "730607229"


def all(a_list: list[int], single_int: int) -> bool:
    """Given a list of ints and an int, return a bool indicating whether or not all the ints in the list are the same as the given int."""
    idx: int = 0
    # idx is short for loop indexing variables.
    if len(a_list) == 0:
        return False
    while idx < len(a_list):
        if a_list[idx] != single_int:
            return False
        else:
            idx += 1
    return True


def max(a_list: list[int]) -> int:
    """Given a list of ints, return the largest in the list."""
    if len(a_list) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    maximum: int = a_list[0]
    while idx < len(a_list):
        if a_list[idx] > maximum:
            maximum = a_list[idx]
        idx += 1
    return maximum


def is_equal(list_a: list[int], list_b: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    idx: int = 0
    if len(list_a) != len(list_b):
        return False
    while idx < len(list_a) or idx < len(list_b):
        if list_a[idx] != list_b[idx]:
            return False
        else:
            idx += 1
    return True


