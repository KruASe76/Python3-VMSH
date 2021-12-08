def main(arg): # Вроде робит..
    max_len = 1
    max_start = 0
    max_end = 0
    temp_len = 1
    temp_start = 0
    temp_end = 0

    for i in range(len(arg)):
        if i == 0:
            continue

        if arg[i] > arg[i-1]:
            temp_len += 1
            temp_end = i
        else:
            if temp_len > max_len:
                max_len = temp_len
                max_start = temp_start
                max_end = temp_end
            temp_len = 1
            temp_start = i
            temp_end = i
    
    return max_len, max_start, max_end
                

length, start, end = main(list(map(float, input().split())))
print()
print(f"Max length of the sequence: {length}\nStarts at index {start}\nEnds at index {end}")