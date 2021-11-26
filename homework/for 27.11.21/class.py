import math
from Euclid import gcd

# Task 1
class OF: # Ordinary Fraction
    def __init__(self, num:int = 0, den:int = 1):
        self.num = num
        self.den = den
    
    def __neg__(self):
        return OF(-self.num, self.den)

    def __add__(self, a):
        if type(a) == OF:
            ans = OF(
                self.num * a.den + a.num * self.den,
                self.den * a.den
            )
            ans.shorten()
            return ans
        elif type(a) == int:
            return self + OF(a)
        else:
            raise TypeError("Addiction/subtraction with this class is not supported")
    
    def __sub__(self, a):
        return self + (-a)

    def __mul__(self, a):
        if type(a) == OF:
            ans = OF(
                self.num * a.num,
                self.den * a.den
            )
            ans.shorten()
            return ans
        elif type(a) == int:
            return self * OF(a)
        else:
            raise TypeError("Miltiplication by this class is not supported")

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def shorten(self):
        divider = gcd(self.num, self.den)
        new_num = int(self.num / divider)
        new_den = int(self.den / divider)
        if new_den < 0:
            new_num = -new_num
            new_den = -new_den
        
        self.num = new_num
        self.den = new_den

# Task 2
class Circle:
    def __init__(self, x:float = 0, y:float = 0, radius:float = 1):
        self.x = x
        self.y = y
        self.radius = radius
    
    def set_radius(self, new_radius:int):
        self.radius = new_radius
    
    def set_x(self, new_x):
        self.x = new_x
    
    def set_y(self, new_y):
        self.y = new_y

    def set_center(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def intersection_points(self, c):
        r1 = self.radius
        r2 = c.radius
        center_distance = math.hypot(abs(self.x - c.x), abs(self.y - c.y))

        if center_distance < r1 and r1 > r2:
            if center_distance + r2 > r1:
                return 2
            elif center_distance + r2 < r1:
                return 0
            else:
                return 1
        elif center_distance < r2 and r2 > r1:
            if center_distance + r1 > r2:
                return 2
            elif center_distance + r1 < r2:
                return 0
            else:
                return 1
        else:
            if r1 + r2 > center_distance:
                return 2
            elif r1 + r2 < center_distance:
                return 0
            else:
                return 1

of1 = OF(4, 3)
of2 = OF(15, -25)
of2.shorten()

print(f"fractions:      {of1}, {of2}")
print(f"substraction:   {of1 - of2}")
print(f"multiplication: {of1 * of2}")
print(f"{of1} - 3:        {of1 - 3}")
print()


# Фото этого ужаса прилагается (circles.jpg)
cir1 = Circle()
cir2 = Circle(radius=2)
cir3 = Circle(2, 2)
cir4 = Circle(-1.5, 0)
cir5 = Circle(0, -0.5, 0.2)
cir6 = Circle(0, -3)
cir7 = Circle(-2, 0, 0.5)
print("1 and 2: ", cir1.intersection_points(cir2))
print("1 and 3: ", cir1.intersection_points(cir3))
print("2 and 3: ", cir2.intersection_points(cir3))
print("1 and 4: ", cir1.intersection_points(cir4))
print("2 and 4: ", cir2.intersection_points(cir4))
print("1 and 5: ", cir1.intersection_points(cir5))
print("4 and 5: ", cir4.intersection_points(cir5)) # просто так
print("4 and 7: ", cir4.intersection_points(cir7))
print("2 and 7: ", cir2.intersection_points(cir7))