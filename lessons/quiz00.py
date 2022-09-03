z: str = "z"
y: str = "y"
x: str = y

y = z
z = x

print(x)
print(y)
print(z)
print(x == z and y == x)