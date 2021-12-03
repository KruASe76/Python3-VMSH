#complex numbers
from math import sqrt, pi, atan, sin, cos

class C_numb:
    def __init__(self,real=1,im=0):
        self.real = real
        self.im = im
        self.mod = sqrt(real**2 + im**2)

        if real>0 and im>=0:
            self.arg = atan(im/real)

        elif real >0 and im<0:
            self.arg = atan(im/real) + 2*pi

        elif real<0 and im>=0:
            self.arg = atan(im/real) + pi

        elif real<0 and im<0:
            self.arg = atan(im/real) + pi

        elif real == 0:
            if im<0:
                self.arg = 2*pi - pi*0.5

            elif im>0:
                self.arg = pi*0.5

    def __add__(self,a):
        if isinstance(a,C_numb):
            return C_numb(self.real + a.real,self.im + a.im)
        else:
            return C_numb(self.real + a,self.im)

    def __radd__(self,a):
        if isinstance(a,C_numb):
            return C_numb(self.real + a.real,self.im + a.im)
        else:
            return C_numb(self.real + a,self.im)
    
    def __sub__(self,a):
        if isinstance(a,C_numb):
            return C_numb(self.real - a.real,self.im - a.im)
        else:
            return C_numb(self.real - a,self.im)

    def __rsub__(self,a):
        if isinstance(a,C_numb):
            return C_numb(a.real - self.real,a.im - self.im)
        else:
            return C_numb(a - self.real, -self.im)

    def __mul__(self,a):
        if isinstance(a,C_numb):
            return C_numb(self.real*a.real - self.im*a.im,self.real*a.im + self.im*a.real)
        else:
            return C_numb(self.real*a,self.im*a)

    def __rmul__(self,a):
        if isinstance(a,C_numb):
            return C_numb(self.real*a.real - self.im*a.im,self.real*a.im + self.im*a.real)
        else:
            return C_numb(self.real*a,self.im*a)

    def con(self):
        return C_numb(self.real,-1*self.im)

    def __truediv__(self,a):
        if isinstance(a,C_numb):
            num = self*a.con()
            denom = (a*a.con()).real
            result = num*(denom**(-1))
            return result
        else:
            return self*(a**(-1))
    
    def __pow__(self, n:int):
        return (self.mod)**n * C_numb(cos(n * self.arg), sin(n * self.arg))

    def root(self, n:int):
        result = []
        for k in range(n):
            new_real = cos((self.arg + 2*pi*k) / n)
            new_im = sin((self.arg + 2*pi*k) / n)
            result.append(str(pow(self.mod, 1/n) * C_numb(new_real, new_im)))
        return result

    def __str__(self):
        return "(%g, %gi)"%(self.real,self.im)

print(C_numb(1, 2).root(3))
print(C_numb(1, 2) * C_numb(3, 4))