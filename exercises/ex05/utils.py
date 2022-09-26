"""EX05 - `list` Utility Functions."""
__author__ = "730607229"


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of ints, return a new list containing only the elements of the input list that were even."""
    # The only_evens function must not modify the list it is given a reference to as a parameter.
    # xs stands for a list.
    i: int = 0
    # i is short for loop indexing variables.
    a_list: list[int] = []
    # assign an empty list
    while i < len(xs):
        if xs[i] % 2 == 0:
            a_list.append(xs[i])
        i += 1
    return a_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """Given two Lists of ints, generate a new List which contains all of the elements of the first list followed by all of the elements of the second list."""
    # concat function may not mutate (“modify”) either of its list parameters.
    new_list: list[int] = []
    i: int = 0
    while i < len(list_a):
        new_list.append(list_a[i])
        i += 1
    i: int = 0
    while i < len(list_b):
        new_list.append(list_b[i])
        i += 1
    return new_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Given a list of ints, a start index, and an end index (not inclusive), generate a List which is a subset of the given list, between the specified start index and the end index - 1."""
    # This function should not mutate its input list.
    new_list: list[int] = []
    # If the length of the list is 0, start is greater than the length of the list, or end is at most 0, return the empty list.
    if len(xs) == 0 or start > len(xs) or end <= 0:
        return new_list
    i: int = start
    alt_i: int = end
    if start < 0:
        i: int = 0
    if end > len(xs):
        alt_i: int = len(xs)
    while i < alt_i:
        new_list.append(xs[i])
        i += 1
    return new_list
