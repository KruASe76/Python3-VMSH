def main():
    n = -1
    s = 0
    counter = -1 # Потому что последний 0 он тоже посчитает
    while n != 0:
        n = float(input())
        s += n
        counter += 1
    
    ans = s / counter

    return int(ans) if ans%1 == 0 else ans


print(main())