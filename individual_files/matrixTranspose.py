__author__ = 'robinjayaswal'

def matrixTranspose(matrix):
    transposedMatrix = []
    for j in range(len(matrix[0])):
        transposedMatrix.append([])
        for i in range(len(matrix)):
            transposedMatrix[j].append(matrix[i][j])

    return transposedMatrix

matrix1 = [[1, 2, 3], [5, 6, 7], [9, 2, 5]]

# matrix:
# 1 2 3
# 5 6 7
# 9 2 5
#
# transpose should be
# 1 5 9
# 2 6 2
# 3 7 5
# aka ((1, 5, 9), (2, 6, 2), (3, 7, 5))
#

print(matrixTranspose(matrix1))