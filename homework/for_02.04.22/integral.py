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

#Если коротко, то метод прямоугольников состоит в том, что мы берем точку по середине промежуточного отрезочка и считаем значение в ней 
#(подменяем нашу функцию на многочлен 0 степени), умножаем полученное значение и это проделываем для всех отрезочков.
#Метод трапеций состоит в подмене на промежуточном отрезке нашей функции уже на линейный многочлен, нашли значения
#функции на концах отрезка, получили трапецию, считаем ее "площадь" (в кавычках, потому что может быть меньше 0, нет
#ведь ограничений на значения функции), так снова делаем для всех отрезочков разбиения. Метод парабол в сущности состоит 
#все в том же, но только подменяем уже на квадратичный многочлен.

def integral_trapezoid(function, left, right, n):
    dx = (right - left) / n
    integral = 0
    for i in range(n):
        integral += (function(left + i*dx) + function(left + (i+1)*dx))/2 * dx
    return integral

print(integral_rectangles(lambda x: 2*x**4 - 5*x**3 - 2*x**2 + 7*x - 3, -5, 5, 1000))
print(integral_parabolas(lambda x: 2*x**4 - 5*x**3 - 2*x**2 + 7*x - 3, -5, 5, 1000))

print(integral_trapezoid(lambda x: 2*x**4 - 5*x**3 - 2*x**2 + 7*x - 3, -5, 5, 1000))