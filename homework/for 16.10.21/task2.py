import math

ax, ay = int(input()), int(input())
bx, by = int(input()), int(input())
cx, cy = int(input()), int(input())
print()

abx = abs(ax - bx)
aby = abs(ay - by)
bcx = abs(bx - cx)
bcy = abs(by - cy)
acx = abs(ax - cx)
acy = abs(ay - cy)

ab = math.hypot(abx, aby)
bc = math.hypot(bcx, bcy)
ac = math.hypot(acx, acy)

if ab >= bc+ac or bc >= ab+ac or ac >= ab+bc:
    print("No")
else:
    print("Yes")