"""Examples of optional parameters and Union types."""

from typing import Union

def hello(name: Union[str, int, float] = "World") -> str:
    """A delightful greeting."""
    greeting: str = "Hello, "
    if isinstance(name, str):
        greeting += name
    elif isinstance(name, int):
        greeting += "COMP" + str(name)
    else:
        greeting += "Alien Life from Sector " + str(name)
    return greeting


# Single-argument
print(hello("Suguru"))

# No arguments!
print(hello())

# int Argument works too!
print(hello(110))
print(hello(3.14))