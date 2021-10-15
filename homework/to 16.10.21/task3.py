import math

a, b, c = int(input()), int(input()), int(input())
print()

d = b**2 - 4*a*c

if d < 0:
    print("There are no roots of the equation with such coefficients")
elif d == 0:
    x = (b*(-1)) / (2*a)
    if x % 1 == 0:
        x = int(x)
    print(f"The single root of the equation is {x}")
else:
    x1 = (b*(-1) - math.sqrt(d)) / (2*a)
    x2 = (b*(-1) + math.sqrt(d)) / (2*a)
    if x1 % 1 == 0:
        x1 = int(x1)
    if x2 % 1 == 0:
        x2 = int(x2)
    print(f"The roots of the equation are {x1} and {x2}")