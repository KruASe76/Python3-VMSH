import multiprocessing as mlp
from random import randint
from time import perf_counter



def generation(length):
    return [randint(10,10000) for i in range(length)]

if __name__ == '__main__': 
    start = perf_counter()
    with mlp.Pool(processes = mlp.cpu_count()) as pool:#тут создаем не отдельных работников, тут сразу создаем толпу
        data = pool.map(generation,[randint(100,100000) for i in range(100)])#поручаем толпе большую задачу, толпа разделит ее сама
        sorted_data = pool.map(sorted,data)
    end = perf_counter()

    print("parallel",end - start)

    start = perf_counter()

    data2 = list(map(generation,[randint(100,100000) for i in range(100)]))#а это последовательная версия наших действий 
    sorted_data2 = list(map(sorted,data))

    end = perf_counter()

    print("not parallel",end - start)


