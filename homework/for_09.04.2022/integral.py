import math
import multiprocessing as mlp
from random import randint
from time import perf_counter


def integral_rectangles(function,left,right,n):
    dx = (right - left)/n
    integral = 0
    for i in range(n):
        integral += function(( 2*left + dx*i + dx*(i+1))/2)*dx

    return integral 

def integral_parabolas(function,left,right,n):
    dx = (right - left)/n
    integral = 0
    for i in range(n):
        integral += (dx/6)*(4*function((2*left + dx*i + dx*(i+1))/2) + function(left+dx*i) + function(left+dx*(i+1)))
    return integral

def integral_parabolas_par(function,left,right,n,q):#queue
    dx = (right - left)/n
    integral = 0
    for i in range(n):
        integral += (dx/6)*(4*function((2*left + dx*i + dx*(i+1))/2) + function(left+dx*i) + function(left+dx*(i+1)))
    q.put(integral)#помещаем значение в очередь 


f = lambda x: ((math.log(x))**3.5)*math.exp(x/3000000)+math.sqrt(math.cos(x)**2)


if __name__ == '__main__': #все ресурсоемкие вычисления будут произведены только если мы напрямую запустим нашу прог, если как модуль импортируем , то ничего вычислять не будем 
    left = 1
    right = 3000000
    n = 6000000

    part = (right - left)/mlp.cpu_count()
    result = 0
    q = mlp.Queue()#создали очередь 
    procs = []#список в котором будем хранить объекты-процессы
    start = perf_counter()

    for i in range(mlp.cpu_count()):
        proc = mlp.Process(target = integral_parabolas_par, args = (f,left + i*part,left+ (i+1)*part,n//mlp.cpu_count(),q))#тут создается очередной процесс-работник
        procs.append(proc)
        proc.start()#тут этот процесс запускается 

    for i in procs:
        i.join()#тут процессы убиваются

    while not q.empty():#проверяем очередь на пустоту
        result+=q.get()#вытаскиваем из очереди элемент (как и в обычных очередях работает)
    end = perf_counter()
    print("parallel",end - start)

    start = perf_counter()

    integral = integral_parabolas(f,left,right,n)

    end = perf_counter()
    print("not parallel",end - start)

    print(result)
    print(integral)




