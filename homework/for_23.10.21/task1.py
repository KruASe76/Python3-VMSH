def main(arg):
    if "," in arg: # Я понял, что то ли все разделители - запятые (мб с пробелом), то ли все пробелы
        arg.replace(" ", "")
        list_arg = arg.split(",")
    else:
        list_arg = arg.split()
    
    for i, elem in enumerate(list_arg):
        list_arg[i] = float(elem)

    s = 0
    for i in list_arg:
        s += i
    
    ans = s / len(list_arg)

    return int(ans) if ans%1 == 0 else ans  # Перфекционизм не лечится


print(main(input()))