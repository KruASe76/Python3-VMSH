def pow_dict(n):
    res = {}
    for i in range(1, n+1):
        res[i] = i**2

    return res

print("Input number:")
n = int(input(">> "))

print(pow_dict(n))