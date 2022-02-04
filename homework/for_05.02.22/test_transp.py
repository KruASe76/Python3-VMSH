from matrix_class import Matrix

A = Matrix(3, 5, [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15], [21, 22, 23, 24, 25]])
B = A.transp_new()
print(f"A\n{A}")
print(f"B\n{B}")
A.transp()
print(f"A\n{A}")