import functools
import matplotlib.pyplot as plt 
from math import *
import struct

from numpy import byte

class Matrix:
    def __init__(self,rows=0,cols=0,matr=None):
        self.rows = rows
        self.cols = cols
        self.matr = matr or []

    def __add__(self,m):
        if (self.rows != m.rows or self.cols != m.cols):
            return "Wrong size"

        res = Matrix(self.rows,self.cols)
        for i in range(self.rows):
            res.matr.append(list(map(lambda x,y:x+y,self.matr[i],m.matr[i])))

        return res

    def __mul__(self,m):
        if isinstance(m,int):
            result = Matrix(self.rows,self.cols)
            for i in range(self.row):
                result.matr.append(list(map(lambda x: m*x, self.matr[i]))   )

        elif isinstance(m,Matrix):
            if (self.cols != m.rows):
                return "Wrong size"

            res = Matrix(self.rows,m.cols)
            for i in range(self.rows):
                tmp=[]
                for j in range(m.cols):
                    c=0
                    for k in range(self.cols):
                        c+=(self.matr[i][k]*m.matr[k][j])
                    tmp.append(c)
                res.matr.append(tmp)
            return res

    @staticmethod
    def findpivot(matr,r,c): #нахождение "опорного элемента"
        for i in range(c,len(matr[0])):
            for j in range(r,len(matr)):
                if matr[j][i]!=0:
                    return [j,i]
        return -1




    def kill(self,r,c,rr):#r,c - опорный элемент,rr - строка, с которой работаем
        if rr!=r:
            l = -1*self.matr[rr][c]/self.matr[r][c] + 1
            self.matr[rr] = list( map(lambda x,y:x+l*y,self.matr[rr],self.matr[r])  )

        for i in range(rr+1,self.rows):
            l = -1*self.matr[i][c]/self.matr[rr][c]
            self.matr[i] = list(  map(lambda x,y:x+l*y,self.matr[i],self.matr[rr])  )

    def __str__(self):
        res=""
        for i in range(self.rows):
            res+= (str(self.matr[i])+"\n")
        return res


    def Triangular(self):
        count = 0

        for i in range(self.rows - 1):
            m = Matrix.findpivot(self.matr, i,count)

            #нашли опорный, теперь приводим i строку в порядок

            if isinstance(m,int):
                return 

            count =m[1] #это столбец, с которого начнем следующий поиск опорного 
            self.kill(m[0],m[1],i)

    def linsolve(self):

        flag_opr = 0
        flag_neopr = 0
        flag_nes = 0

        if self.rows<self.cols - 1:
            flag_neopr = 1

        self.Triangular()
        for i in range(self.rows - 1,-1,-1):
            if self.matr[i][i] == 0:
                flag_neopr = 1
                break

            if ( functools.reduce(lambda y,x:y+x*x,self.matr[i])  ) == (self.matr[i][-1])**2 and (self.matr[i][-1])!=0:
                flag_nes = 1
                break

        if flag_nes == 0 and flag_neopr == 0:
            s = [0 for i in range(self.cols - 1)]#изначально список нулей
            #[x1,x2,...,xn]

            for i in range(self.cols -2,-1,-1):
                s[i] = (sum( (map(lambda x,y:x*(-y),s,self.matr[i]) )) + self.matr[i][-1]/self.matr[i][i] )

            return s

    def Determinant(self):
        if self.rows!=self.cols:
            return "Mistake"
        self.Triangular()
        det = 1

        for i in range(self.cols):
            det*=self.matr[i][i]
        return det 

    def Transpose(self):
        tmp = []
        for i in range(self.cols):
            m=[]
            for j in range(self.rows):
                m.append(self.matr[j][i])
            tmp.append(m)
        self.matr=tmp
        self.rows,self.cols = self.cols,self.rows


#чтение изображения, читаем его как массив байтов
f=open('image.bmp','rb')
data = bytearray(f.read())
f.close()

bmp_data_offset = 54#сдвиг, с этого байта начинается информация о пикселях

#кортеж с инфой из первых 54 байт изображения(файла)
bmp_info = struct.unpack_from('cc',data,offset = 0) + struct.unpack_from('i H H i',data,offset = 2) + struct.unpack_from('i i i H H i i i i i i',data,offset = 14)

#двумерный массив пикселей (пиксель - тройка чисел от 0 до 255)
mass = []
for i in range(bmp_info[8]):
    tmp = []
    for j in range(bmp_info[7]):
        pos = bmp_data_offset + ceil(  (bmp_info[10]*bmp_info[7])/32)*4*i + j*3
        pixel_info=tuple(data[pos:pos+3])# инфа о конкретном пикселе, 3 числа от 0 до 255 (RGB)
        tmp.append(pixel_info)
    mass.append(tmp)

img = Matrix(bmp_info[8],bmp_info[7],mass)#создал матрицу пикселей (только пиксели и ничего больше)

img.Transpose()#транспонируем массив пикселей

#создание нового файла с транспонированным (повернутым изображение)
f = open('new_image.bmp','wb')

transp_row_size = ceil( (24*img.cols)/32 )*4 #посчитали размер строки в новом изображении в байтах
true_size = 54 + transp_row_size*img.rows #полный размер нового изображения в байтах

#в массив байт, который будет записан в новый файл, записываются 54 байта информации о новом изображении (важно, что это самые первые 54 байта)
data_transp = bytearray(bmp_info[0]+bmp_info[1] + true_size.to_bytes(4,'little') + bmp_info[3].to_bytes(2,'little')+ bmp_info[4].to_bytes(2,'little') + bmp_data_offset.to_bytes(4,'little')+bmp_info[6].to_bytes(4,'little') + bmp_info[8].to_bytes(4,'little')+ bmp_info[7].to_bytes(4,'little')+bmp_info[9].to_bytes(2,'little')+bmp_info[10].to_bytes(2,'little')+bmp_info[11].to_bytes(4,'little')+(true_size - 54).to_bytes(4,'little')+bmp_info[13].to_bytes(4,'little') + bmp_info[14].to_bytes(4,'little')+bmp_info[15].to_bytes(4,'little')+bmp_info[16].to_bytes(4,'little'))

bitmap_data = []
for row in img.matr:
    for pixel in row:
        bitmap_data += list(pixel)
    if len(row)*3 % 4 != 0:
        bitmap_data += [0] * (4 - len(bitmap_data)%4)

# print(bitmap_data)


#надо записать data_transp в файл

f.write(data_transp + bytearray(bitmap_data))
f.close()

# Теперь все робит короче