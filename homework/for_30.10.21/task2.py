def gcd_without_recursion_pro(lst): # ВОТ ЭТО заработало с ПЕРВОГО РАЗА [можете меня поздравить]
    while 0 in lst:
        lst.remove(0)
    
    lst = list(set(lst)) # Не уверен, что это необходимо, но лучше перестраховаться и избавиться от лишних проблем
    
    while len(lst) > 1:
        divider = min(lst)
        for i, elem in enumerate(lst):
            if elem != divider:
                lst[i] %= divider
        while 0 in lst:
            lst.remove(0)
    
    return divider

lst = list(map(int, input().split()))
print()
print(gcd_without_recursion_pro(lst))