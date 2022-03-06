
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


    @staticmethod
    def GCD(a,b): #Нахождение НОД многочленов, сам алгоритм не отличается от алгоритма Евклида для чисел, только теперь сравниваются степени 
        while b.coefs!=[0] and a.coefs!=[0]:
            if len(a.coefs)>len(b.coefs):
                a=a%b
                a.simplify()# чтобы в старших степенях не было лишних нулей, мешает проведению деления с остатком 
            else:
                b=b%a
                b.simplify()
        return a+b

    def FindValue(self,point):
        result = 0
        for i in range(len(self.coefs)):
            result+= self.coefs[i]*(point**i)

        return result

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

#строим систему Штурма
def FindSturm(polynom):
    SturmSys = []

    SturmSys.append(polynom)
    SturmSys.append(polynom.derivative())

    while True:

        k = -1*(SturmSys[-2]%SturmSys[-1])

        SturmSys.append(k)

        if len(k.coefs) == 1:
            break

    return SturmSys

#Штурмуем многочлен на отрезке (зачеркнуть) считаем количество корней на отрезке с помощью системы Штурма 
def RootCount(SturmSys,left,right):
    SignLeft = []
    SignRight = []
    ChangeLeft = 0
    ChangeRight = 0

    for i in SturmSys:
        ValLeft = i.FindValue(left)
        ValRight = i.FindValue(right)

        if ValLeft > 0:
            SignLeft.append(1)
        elif ValLeft<0:
            SignLeft.append(-1)

        if ValRight > 0:
            SignRight.append(1)
        elif ValRight<0:
            SignRight.append(-1)

    for i in range(1,len(SignLeft)):
        if SignLeft[i-1]!=SignLeft[i]:
            ChangeLeft+=1

    for i in range(1,len(SignRight)):
        if SignRight[i-1]!=SignRight[i]:
            ChangeRight+=1

    return ChangeLeft - ChangeRight


def RootTop(polynom):
    coefs = polynom.coefs[::-1]
    max_degree_coef = coefs[0]
    coefs = list(map(lambda a: a / max_degree_coef, coefs))

    for i in range(len(coefs)):
        if coefs[i] < 0:
            m = i
            break
    else:
        return None
    
    negative_coefs_abs = []
    for coef in coefs:
        if coef < 0:
            negative_coefs_abs.append(abs(coef)) 
    b = max(negative_coefs_abs)

    return 1 + b**(1/m)

def RootBottom(polynom):
    return -RootTop(Polynom(list(map(lambda coef, ind: -coef if (len(polynom.coefs) - ind - 1) % 2 == 0 else coef, polynom.coefs, range(len(polynom.coefs))))))

print(RootTop(Polynom((3, -2, 1, 1))))
print(RootBottom(Polynom((3, -2, 1, 1))))
# по идее: первый и единственный отрицательный коэф - это -2, стоит на 2 месте
# зачит, 1 + √2, все верно
# только нормального онлайн-калькулятора я так и не нашел, чтоб проверить...