
from tkinter import Place


class Polynom:
    def __init__(self,coefs=None):
        self.coefs = coefs or [0] #by default [const,x,x^2,...,x^n]

    def __add__(self, poly):
        res = Polynom(list(map(lambda x,y:x+y,self.coefs, poly.coefs))) #сначала сложили коэффициенты до самого старшего у многочлена наименьшей степени
        res.coefs.extend(self.coefs[len(poly.coefs):] if len(self.coefs)>len(poly.coefs) else poly.coefs[len(self.coefs):]) #остались коэффициенты многочлена наибольшей степени, их просто в конец списка добавляем
        return res #строчкой выше использовал тернарный оператор, в целом можно обычные ифы использовать 

    def __mul__(self,arg):
        if isinstance(arg,int) or isinstance(arg,float):
            return Polynom(list(map(lambda x:x*arg,self.coefs)))#умножение на число 

        else:
            res = Polynom([0 for i in range(len(self.coefs) + len(arg.coefs) - 1)])
            for i in range(len(self.coefs)):
                for j in range(len(arg.coefs)):
                    res.coefs[i+j]+= self.coefs[i]*arg.coefs[j] #умножение многочленов 
            return res

    def __rmul__(self,arg): #чтоб можно было умножить число на многочлен (const*poly)
        if isinstance(arg,int) or isinstance(arg,float):
            return Polynom(list(map(lambda x:x*arg,self.coefs)))


    def simplify(self):
        while self.coefs[-1]==0 and len(self.coefs)>1:
            self.coefs=self.coefs[:-1]#коротенькая функция, убирающая лишние нули в старших степенях, список при этом укорачивается,меняет вызвавший ее объект 

    def __sub__(self,arg):# вычитание на базе умножения на константу и сложения
        res = self + (-1)*arg
        return res

    def __floordiv__(self,arg):
#реализация максимально простая, на полную используем уже готовые элементы класса и приближаем процесс деления к тому, что мы делаем на бумаге
#из негативного - тут создается копия делимого (благо один раз) и на каждой итерации создается новый многочлен s
#во избежание такого, можно пробовать проводить манипуляции над списками, но код для понимания будет сложнее

        if len(self.coefs)<len(arg.coefs):# случай если степень делимого меньше степени делителя 
            return Polynom([0])

        res = Polynom([0 for i in range(len(self.coefs) - len(arg.coefs)+1)])#то, куда будем постепенно складывать коэф-ты результата
        buf = Polynom(self.coefs)#копия делимого, которую мы будем изменять 

        for i in range(len(res.coefs)-1,-1,-1):
            res.coefs[i] = buf.coefs[-1]/arg.coefs[-1] #определяем очередной коэффициент в неполном частном
            s = Polynom([0 for j in range(i+1)])# в полной аналогии с делением на бумаге берем только что подобранные коэффициент и степень (одно слагаемое в записи результата)

            s.coefs[-1] = res.coefs[i]
            buf = buf - s*arg#в очередной раз изменяем копию, понижая ее степень на 1 гарантированно 
            buf.coefs = buf.coefs[:len(buf.coefs) - 1]# обрезаем лишний 0


        res.simplify()#на всякий случай обрезаем возможные нули
        return res


    def __mod__(self,arg):#остаток от деления двух многочленов, потому что f=p*g + r -> r = f - p*g
        if len(self.coefs)<len(arg.coefs):
            return self

        else:
            res = self - arg*(self//arg)
            res.simplify()#могут возникнуть лишние нули, потому что есть вычитание 
            return res

    def derivative(self):
        res = Polynom([0 for i in range(len(self.coefs) - 1)])#производная от многочлена

        for i in range(len(self.coefs) - 1):
            res.coefs[i] = self.coefs[i+1]*(i+1)

        return res


    def __str__(self):
        res = ""
        for i in range(len(self.coefs)-1,-1,-1):
            if self.coefs[i] == 0:
                continue
            elif abs(self.coefs[i]) == 1:
                if self.coefs[i] == -1:

                    res+=" - x^{}".format(i)

                else:
                    res+=" + x^{}".format(i)

            else:
                if self.coefs[i]>0:
                    res+=" + {}x^{}".format(self.coefs[i],i)

                else:
                    res+=" - {}x^{}".format(abs(self.coefs[i]),i)

        return res
    
    @classmethod
    def NOD(cls, pol1, pol2):
        # no check? okay

        if [0] in (pol1.coefs, pol2.coefs):
            return pol1 + pol2
        
        pol1.simplify()
        pol2.simplify()
        
        if len(pol1.coefs) < len(pol2.coefs):
            pol1, pol2 = pol2, pol1
        
        return cls.NOD(pol1 % pol2, pol2)






print(Polynom((-1, -1, 1, 0, 5, 10, -8, 0, 78, 0))) # /злой смех/ я сломал Ваш вывод

print(Polynom.NOD(Polynom([4, 4, 1]), Polynom([2, 1])))
print(Polynom.NOD(Polynom([4, 6, 8]) * 5, Polynom([2, 3, 4] * 2)))
print(Polynom.NOD(Polynom([-9, -12, -3, 2, 0, 9, 1]), Polynom([-3, 2, 10, 1]))) # дефолтный пример с https://abakbot.ru/online-16/447-nodpol
# и вообще, во всех калькуляторах список коэфов идет со старшей степени
# \ /
# . .
#  ^