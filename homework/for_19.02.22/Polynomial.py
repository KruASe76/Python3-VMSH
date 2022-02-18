from audioop import mul
from re import M

def custom_sum(iter):
    iter = tuple(iter)
    res = iter[0]
    for elem in iter[1:]:
        res += elem
    return res

def to_superscript(num): # with "x"
    if num == 0:
        return ""
    if num == 1:
        return "x"

    SUPERSCRIPT = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = "x"
    for digit in str(num):
        res += SUPERSCRIPT[int(digit)]
    return res


class Multicock(): # Не бейте за шутку пж
    def __init__(self, *coeffs: float):
        try:
            iter(coeffs[0])
        except TypeError:
            pass
        except IndexError:
            pass
        else:
            if not isinstance(coeffs[0], str):
                coeffs = coeffs[0]
        
        coeffs = list(coeffs)

        for ind, coeff in enumerate(coeffs):
            coeff = float(coeff)
            coeffs[ind] = int(coeff) if coeff % 1 == 0 else coeff

        self.coeffs = coeffs
        self.max_degree = len(self.coeffs) - 1
    
    def __str__(self): # однострочный челлендж комплит
        return " + ".join(filter(lambda elem: elem, map(lambda coeff, ind: f"{coeff if abs(coeff) != 1 or ind == 0 else str(coeff)[:-1]}{to_superscript(ind)}" if coeff else "", self.coeffs, range(self.max_degree, -1, -1)))).replace("+ -", "- ") if self.coeffs else "0"
    
    def __add__(self, other):
        if not isinstance(other, Multicock):
            other = Multicock(other)

        if self.max_degree > other.max_degree:
            other_coeffs = [0] * (self.max_degree - other.max_degree) + other.coeffs
            self_coeffs = self.coeffs
        elif self.max_degree < other.max_degree:
            self_coeffs = [0] * (other.max_degree - self.max_degree) + self.coeffs
            other_coeffs = other.coeffs
        else:
            self_coeffs = self.coeffs
            other_coeffs = other.coeffs

        return Multicock(map(lambda a, b: a + b, self_coeffs, other_coeffs))
    
    def __sub__(self, other):
        if not isinstance(other, Multicock):
            other = Multicock(other)
        
        return self + Multicock(map(lambda coeff: -coeff, other.coeffs))

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Multicock(map(lambda a: a * other, self.coeffs))

        if not isinstance(other, Multicock):
            other = Multicock(other)
        
        return custom_sum(map(lambda coeff: Multicock((other * coeff).coeffs + [0] * (self.max_degree - self.coeffs.index(coeff))), self.coeffs))

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self * (1/other)
        
        if not isinstance(other, Multicock):
            other = Multicock(other)

        temp_divisible = self
        res = []
        while temp_divisible.max_degree >= other.max_degree:
            multiplier = temp_divisible.coeffs[0] / other.coeffs[0]
            temp_divisible = temp_divisible - Multicock(other.coeffs + [0] * (temp_divisible.max_degree - other.max_degree)) * multiplier
            res.append(multiplier)
            temp_divisible.coeffs.pop(0)
            temp_divisible.max_degree -= 1
        
        return Multicock(res), temp_divisible
    
    def diff(self):
        return Multicock(map(lambda coeff, ind: coeff * ind, self.coeffs[:-1], range(self.max_degree, 0, -1)))





if __name__ == "__main__":
    mc1 = Multicock("-1", 2, "-3.5", 4, -0, 0, 56, 8456, 1, "48561", -1, -1)
    print(mc1.coeffs)
    print(mc1)
    print()

    mc2 = Multicock(1, -2, 3, -4, 5)
    print(mc1 + mc2)
    print(mc2 - mc1)
    print()

    mc3 = Multicock(5, 15, 23, -8)
    print(mc2 * 5)
    print(mc2 * mc3)
    print()
    
    print(mc3 / 4)
    mc4 = Multicock(3, -5, 10, -3)
    mc5 = Multicock(3, 1)
    print(*(mc4 / mc5), sep="; ") # Первые примеры, если забить в Яндексе "деление многочленов"
    mc6 = Multicock(4, 0, -3, 0, 1, -1)
    mc7 = Multicock(2, 0, -3)
    print(*(mc6 / mc7), sep="; ") # и открыть картинки (для отладки промежуточных результатов)
    print()

    print(mc2.diff())