"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730607229"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Returns the distance between the Point object the method was called on and some other Point object passed in as a parameter."""
        distance: float = 0.0
        distance = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Reassign the object's location attribute, the result of adding the self object's location with its direction."""
        self.location = self.location.add(self.direction)
        # self.location = self.direction.add(self.location)
        if self.is_infected():
            self.sickness += 1
            if self.sickness > constants.RECOVERY_PERIOD:
                self.immunize()

    def contract_disease(self) -> None:
        """Assign the INFECTED constant to the sickness attribute of the Cell object."""
        self.sickness = constants.INFECTED
    
    def immunize(self) -> None:
        """Assign the constant IMMUNE to the sickness attribute of the Cell object."""
        self.sickness = constants.IMMUNE
    
    def is_vulnerable(self) -> bool:
        """Return True when the cell's sickness attribute is equal to VULNERABLE and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Return True when the cell's sickness attribute is equal to INFECTED and False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def is_immune(self) -> bool:
        """Return True when the Cell object's sickness attribute is equal to the IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_infected():
            return "red"
        if self.is_immune():
            return "lime green"
        return "gray"

    def contact_with(self, other: Cell) -> None:
        """If either of the Cell objects is infected and the other is vulnerable, then the other should become infected."""
        if self.is_infected() and other.is_vulnerable():
            other.contract_disease()
        if self.is_vulnerable() and other.is_infected():
            self.contract_disease()


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if infected_cells <= 0:
            raise ValueError("Cell objects that begin infected should not be 0 or negative.")
        if infected_cells >= cells:
            raise ValueError("Cell objects that begin infected should not be equal to or exceeds the value of the cells parameter.")
        if immune_cells < 0:
            raise ValueError("Cell objects that begin immuned should not be negative.")
        if immune_cells >= cells:
            raise ValueError("Cell objects that begin immuned should not be equal to or exceeds the value of the cells parameter.")
        if infected_cells + immune_cells > cells:
            raise ValueError("Total number of infected cells and immune cells should not exceeds the cells parameter.")
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for i in range(infected_cells):
            cell = self.population[i]
            cell.contract_disease()
        for alt_i in range(infected_cells, infected_cells + immune_cells):
            cell = self.population[alt_i]
            cell.immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True
    
    def check_contacts(self) -> None:
        """Compare the distance between every two Cell objects' location attributes in the population.If any distance between two Cells is less than the constant CELL_RADIUS, then call the Cell#contact_with method on one of the two Cell objects, giving a reference to the other as an argument."""
        for i in range(len(self.population)):
            for alt_i in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[alt_i].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[alt_i])