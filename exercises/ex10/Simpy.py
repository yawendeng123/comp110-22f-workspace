"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730607229"


class Simpy:
    """A simpler, single dimension implementation of many of the same capabilities of Numpy."""

    values: list[float]

    def __init__(self, values: list[float]):
        """Construct a values attribute of the newly constructed Simpy object to the argument passed in."""
        self.values = values
    
    def __repr__(self) -> str:
        """Special method will automagically be called when a Simpy object is converted to a str representation."""
        return f"Simpy({self.values})"
    
    def fill(self, value: float, repeat: int) -> None:
        """Fill a Simpy's values with a specifc number of repeating values."""
        self.values = []
        for _ in range(repeat):
            self.values.append(value)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values in terms of floats."""
        assert step != 0.0
        length = int((stop - start) / step)
        for i in range(length):
            self.values.append(start + step * i)
    
    def sum(self) -> float:
        """Compute and return the sum of all items in the values attribute."""
        a_sum: float = sum(self.values)
        return a_sum
    
    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overload the addition operator for Simpy + Simpy or Simpy + float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] + rhs.values[i])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        return result
    
    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Overload the power operator for Simpy ** Simpy or Simpy ** float."""
        result: Simpy = Simpy([])
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.values.append(self.values[i] ** rhs.values[i])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        return result
    
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produce a mask or list[bool] based on the equality (==) of each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] == rhs.values[i])
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        return result
    
    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Produce a mask or list[bool] based on the greater than relationship (>) between each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for i in range(len(self.values)):
                result.append(self.values[i] > rhs.values[i])
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload subscription notation with Simpy objects."""
        if isinstance(rhs, int):
            assert rhs >= 0 and rhs < len(self.values)
            result = self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            result = Simpy([])
            for i in range(len(rhs)):
                if rhs[i]:
                    result.values.append(self.values[i])
        return result
