"""List diagram example."""


a: list[str] = ["one"]
b: list[str] = a
a.append("two")

print(b[1])
# If append on b, it will also append on a.
# in the environmental diagram, you can choose whether add "" around the output or not, it will not affect.


def dup(xs: list[int]) -> None:
    """Duplicate a list's values."""
    start_len: int = len(xs)
    i: int = 0
    while i < start_len:
        xs.append(xs[i])
        i += 1


nums: list[int] = [10, 20]
dup(nums)
print(nums)


"""Example producing a function."""

def odds(min: int, max: int) -> list[int]:
    """Construct list of odds, inclusive."""
    xs: list[int] = list()
    i: int = (min//2) * 2 + 1
    while i <= max:
        xs.append(i)
        i += 2
    return xs


ys: list[int] = odds(3, 6)
print(ys)