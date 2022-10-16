"""Notes and examples of tuple and range sequences."""

# An example of a tuple without type aliasing
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they're ordered, 0-indexed
print(goat[0])
print(goat[1])

# Printing a tuple produces its literal syntax
print(goat)

# Print both items on the same line
print(f"{goat[0]} is number {goat[1]}")

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for...in loops
# Meaning you can loop over them with for...in
for item in goat:
    print(item)

# Tuples, unlike lists, are immutable
# Which means we cannot reassigns items, nor append, not pop, etc
# goat[0] = "LBJ" 

# We can "invent" our own type with a type alias
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a strange world, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)


# A range is another common sequence type
zero_to_nine: range = range(0, 10, 1)

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)


# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


# Declaring a type alias that "invents" the Point2D type
Point2D = tuple[float, float]
# Camel Casing: not underscores_between two words.
start_position: Point2D = (5.0, 10.0)
# we cannot simply reassign a tuple, we should create a new one like this below.
start_position = (start_position[0] + 5.0, start_position[1] + 10.0)
end_position: Point2D = (99.0, 99.0)

# tuples, because they are a sequence, are 0-indexed
print(start_position[0])

for item in end_position:
    print(item)

print(len(end_position))


# examples of ranges
a_range: range = range(0, 10 , 1)
# access its items:
print(a_range[0])
print(a_range[1])
print(len(a_range))
for i in a_range:
    print(i)

# an example of using the default parameter step
# where the default step is 1
another_range: range = range(0, 10)

# If you only pass one argument to range, it specifies the stop marker and start is 0 by default.
zero_start: range = range(10)
for x in zero_start:
    print(x)

names: list[str] = ["Evelina", "Karmen", "Olivia", "Coco"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")

# range is often used to write for loops where your iteration pattern is not consecutive.
print("Every other")
for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")

print(odds_to_99.stop)