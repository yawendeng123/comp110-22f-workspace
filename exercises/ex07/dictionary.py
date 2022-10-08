"""EX07 - Dictionary Functions."""
__author__ = "730607229"


def invert(initial: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values. The keys of the input list becomes the values of the output list and vice versa."""
    result: dict[str, str] = {}
    check: list[str] = []
    for i in initial:
        if initial[i] not in check:
            check.append(initial[i])
    if len(check) != len(initial):
        raise KeyError("Keys in a dictionary should be unique")
    for key in initial:
        result[initial[key]] = key
    return result


def count(xs: list[str]) -> dict[str, int]:
    """Given a list[str], produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    counter_dictionary: dict[str, int] = {}
    for i in xs:
        if i in counter_dictionary:
            counter_dictionary[i] += 1
        else:
            counter_dictionary[i] = 1
    return counter_dictionary


def favorite_color(colors: dict[str, str]) -> str:
    """Given a dictionary of [str, str] of names and favorite colors, return a str which is the color that appears most frequently. If there is a tie for most popular color, return the color that appeared in the dictionary first."""
    counter: dict[str, int] = {}
    value_list: list[str] = []
    for key in colors:
        value_list.append(colors[key])
    for i in value_list:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    key_list: list[str] = []
    for key in counter:
        key_list.append(key)
    maximum: int = 0
    popular: str = ""
    for key in counter:
        popular = key_list[0]
        if counter[key] > maximum:
            maximum = counter[key]
            popular = key
    return popular
