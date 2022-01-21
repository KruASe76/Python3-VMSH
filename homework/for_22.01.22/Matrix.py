class Matrix:
    def __init__(self, rows=0, cols=0, matr=[]): #тут matr предполагается 2-мерным массивом
        self.rows = rows
        self.cols = cols
        self.matr = matr
 
    def __add__(self, other):
        if not(isinstance(other, Matrix)):
            other_type = str(type(other))[8:-2]
            raise TypeError(f"unsupported operand type(s) for +: 'Matrix' and '{other_type}'")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("sizes of adding matrixes are different")
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            result.matr.append(list(map(lambda x, y: x+y, self.matr[i], other.matr[i])))
        return result
 
    def __mul__(self, other):
        if isinstance(other, int):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                result.matr.append(list(map(lambda x: other*x, self.matr[i])))
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("amount of first matrix columns should equal to amount of second matrix rows")
            result = Matrix(self.rows, other.cols)
            other_zip = list(zip(*other.matr))
            result.matr = [[sum(a*b for a, b in zip(self_row, other_col)) for other_col in other_zip] for self_row in self.matr]
            
        return result

if __name__ == "__main__":
    print((Matrix(2, 2, [[1, 2], [3, 4]]) * Matrix(2, 1, [[5], [6]])).matr)