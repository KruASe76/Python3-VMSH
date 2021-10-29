def gcd_without_recursion(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return a if a != 0 else b

a = int(input())
b = int(input())
print()
print(gcd_without_recursion(a, b))
