"""Tracing Loops Practice Question."""

i: int = int(input("Give a # > 0: "))
s: str = ""

while i > 0:
    s = s + "h"
    h: int = 0
    while h < i:
        s = s + "e"
        h = h + 1
    i = i - 1

print(s)