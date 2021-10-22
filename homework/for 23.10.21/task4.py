def custom_max(arg):
    temp_max = arg[0]
    for i in arg:
        if i > temp_max:
            temp_max = i
    
    return int(temp_max) if temp_max%1 == 0 else temp_max

def custom_min(arg):
    temp_min = arg[0]
    for i in arg:
        if i < temp_min:
            temp_min = i
    
    return int(temp_min) if temp_min%1 == 0 else temp_min


l = list(map(float, input().split())) # Только для ввода

print(f"Max: {custom_max(l)}")
print(f"Min: {custom_min(l)}")