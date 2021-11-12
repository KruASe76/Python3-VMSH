# (Дублирую README.md)
# Решил сделать оба задания в одном файле, ибо для бинарного поиска нужен уже отсортированный массив.
# Да, можно было импортнуть сортировку из файла с заданием 2, но я.. как бы использую в первом задании
# то, что сделал во втором, то есть после первого.. короче криво, и в одном файле проще.
# Сортировка, которую я написал - Comb Sort (сортировка расческой) (около 10.5 секунд на 10^6 элементов)

import time, random

# Task 1
def bin_search_recursion(l, x):
    if len(l) == 0:
        return -1
    else:
        mid = len(l) // 2
        if x == l[mid]:
            return mid
        elif x < l[mid]:
            return bin_search_recursion(l[:mid], x)
        else:
            next_iter_result = bin_search_recursion(l[mid+1:], x)
            if next_iter_result == -1:
                return -1
            else:
                return bin_search_recursion(l[mid+1:], x) + mid + 1


# Task 2
def comb_sort(l):
    step = len(l) - 1
    k = 1.24733095
    done = False
    while not done:
        step = int(step)
        if step == 1:
            done = True
        for i in range(len(l)-step):
            if l[i] > l[i+step]:
                temp = l[i]
                l[i] = l[i+step]
                l[i+step] = temp
                done = False
        
        if step > 1:
            step //= k
    
    return l


print("Selet the action:\n1 - Sort list and search in sorted\n2 - Only sort the list")
reply1 = int(input(">> "))

if reply1 not in [1, 2]:
    print("\nInvalid option")
    print("Program finished")
    exit()

print("\nSelect the way to get the list:\n1 - Input (within one string, space separating)\n2 - Fill with random numbers from -(10^9) to 10^9")
reply2 = int(input(">> "))

if reply2 == 1:
    print("\nInput the list:")
    l = list(map(int, input(">> ").split()))
elif reply2 == 2:
    print("\nInput amount of numbers in the list:")
    count = int(input(">> "))
    l = []
    for _ in range(count):
        l.append(random.randint(-(10**9), 10**9))
else:
    print("\nInvalid option")
    print("Program finished")
    exit()

print("\nOutput the list? (y/n)")
reply3 = input(">> ")
if reply3.lower() not in 'yn':
    print("\nInvalid option")
    print("Program finished")
    exit()

start_sort = time.time()
sorted_l = comb_sort(l)
end_sort = time.time()

print("\nSorted list:")
if reply3.lower() == "y":
    print(*sorted_l)
print(f"Time spent: {end_sort - start_sort} seconds")

if reply1 == 1:
    print("\nInput number to search:")
    x = int(input(">> "))

    start_search = time.time()
    pos = bin_search_recursion(sorted_l, x)
    end_search = time.time()

    if pos == -1:
        print("\nThe number is not in the list")
    else:
        print(f"\nNumber index: {pos}")
    print(f"Time spent: {end_search - start_search} seconds")

print("\n\nProgram finished")