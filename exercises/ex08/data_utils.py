"""Dictionary related utility functions."""

__author__ = "730607229"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows, each row represented as dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a `list[str]` of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows (e.g. `list[dict[str, str]]`) into one represented as a dictionary of columns (e.g. `dict[str, list[str]]`)."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Given a column-based table of data and number of rows to conclude in the result, produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in table:
        storage: list[str] = []
        i: int = 0
        alt_n: int = n
        if n > len(table[column]):
            alt_n = len(table[column])
        while i < alt_n:
            storage.append(table[column][i])
            i += 1
        result[column] = storage
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new-column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in names:
        result[column] = table[column]
    return result


def concat(table_a: dict[str, list[str]], table_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in table_a:
        result[column] = table_a[column]
    for column in table_b:
        if column in result:
            i: int = 0
            while i < len(table_b[column]):
                result[column].append(table_b[column][i])
                i += 1
        else:
            result[column] = table_b[column]
    return result


def count(xs: list[str]) -> dict[str, int]:
    """Given a list[str], produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for i in xs:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result
