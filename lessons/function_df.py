"""An example of funtion definition."""


def my_max(a: int, b:int) -> int:
    # signature line(contrast line)
    """Returns the largest argument."""
    # docstring
    if a >= b:
        return a
    else:
        return b
    # body block

x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)
