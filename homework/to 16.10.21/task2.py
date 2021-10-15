ax, ay = int(input()), int(input())
bx, by = int(input()), int(input())
cx, cy = int(input()), int(input())
print()

if (ax == bx and bx == cx) or (ay == by and by == cy):
    print("No")
else:
    print("Yes")