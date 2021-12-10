# the n-dimensional vector class

import math

class Vector():
    @staticmethod
    def check_if_vector(arg, action:str = ""):
        if type(arg) != Vector:
            try:
                arg = Vector(*tuple(arg))
                if action:
                    return arg
                else:
                    return True
            except:
                if action:
                    raise TypeError(f"{action} with this type is not supported")
                else:
                    return False
        if action:
            return arg
        else:
            return True


    def __init__(self, *coords:float):
        self.coords = coords
        self.dism = len(coords)

        self.norm = math.sqrt(self * self)
    
    @classmethod
    def fromseq(cls, seq): # from sequence
        return Vector(*seq)


    def __add__(self, other): # __radd__ method is useless, because addition only with vector is allowed
        other = Vector.check_if_vector(other, "addition")

        if self.dism != other.dism:
            raise TypeError("vectors should be the same dismention")
        
        return Vector(*map(lambda a, b: a + b, self.coords, other.coords))
    
    def __mul__(self, other):
        if type(other) in (int, float): # multiplication by number
            return Vector(*map(lambda a: a * other, self.coords))

        # scalar multiplication
        other = Vector.check_if_vector(other, "multiplication")
        
        if self.dism != other.dism:
            raise TypeError("vectors should have the same dism")
        
        return sum(map(lambda a, b: a * b, self.coords, other.coords))
    
    def __rmul__(self, other): # only for number
        if type(other) not in (int, float):
            other_type = str(type(other))[8:-2]
            raise TypeError(f"unsupported operand type(s) for *: '{other_type}' and 'Vector'")
        
        return Vector(*map(lambda a: a * other, self.coords))
    

    def __eq__(self, other):
        other = Vector.check_if_vector(other, "comparison")
        return self.coords == other.coords
    
    def __ne__(self, other):
        other = Vector.check_if_vector(other, "comparison")
        return self.coords != other.coords


    def __str__(self):
        self.coords = tuple(int(a) if a % 1 == 0 else a for a in self.coords) # i like Python :)
        return str(self.coords)

    
    @staticmethod
    def angle(arg1, arg2):
        arg1 = Vector.check_if_vector(arg1, "angle function")
        arg2 = Vector.check_if_vector(arg2, "angle function")
        return math.degrees(math.acos((arg1 * arg2) / (arg1.norm * arg2.norm)))

def test():
    v = Vector(1, 2, 3.5)
    v1 = Vector.fromseq((1, 2, 3.5))
    print(f"v == v1:          {v == v1}")
    print(f"v:                {v}")
    print(f"v + v:            {v + v}")
    print(f"v + [5, 7, 145]:  {v + [5, 7, 145]}")
    print(f"v * 10:           {v * 10}")
    print(f"5.8 * v:          {5.8 * v}")
    print()

    a = Vector(1, 3, -5)
    b = Vector(4, -2, -1) # example from Wikipedia
    print(f"a * b:            {a * b}")
    print(f"angle(a, b):      {Vector.angle(a, b)}")
    print()

    c = Vector(5, -2, 7)
    print(f"c.norm:           {c.norm}")


if __name__ == "__main__":
    test()