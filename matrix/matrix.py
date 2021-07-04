import numpy as np


class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = [[int(j) for j in i.split()]
                              for i in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix_string[index-1]
        # return self.matrix_string[index-1]

    def column(self, index):
        return [r[index-1]for r in self.matrix_string]
        # return self.matrix_string[:, index-1]

    def __str__(self):
        return f"{self.matrix_string}"


matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
print(matrix.row(1))
print(matrix.column(1))
