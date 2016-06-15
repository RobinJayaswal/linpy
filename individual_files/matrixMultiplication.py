__author__ = 'robinjayaswal'

def multiplyMatrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Error: cannot multiply " + len(matrix1) +  "x" + len(matrix1[0]) + " matrix by " + len(matrix2) +  "x" + len(matrix2[0]) + " matrix")
        return

    resultantMatrix = []

    for i in range(len(matrix1)):
        resultantMatrix.append([])
        for k in range(len(matrix2[0])):
            sum = 0
            for j in range(len(matrix1[0])):
                sum += matrix1[i][j] * matrix2[j][k]
            resultantMatrix[i].append(sum)
    return resultantMatrix

matrix1 = [[1, 2, 3], [5, 6, 7], [9, 2, 5]]
matrix2 = [[10, 10, 10], [1, 2, 1], [5, 5, 5]]

print(multiplyMatrices(matrix1, matrix2))


#
#1 2 3      10 10 10
#5 6 7      1 2 1
#9 2 5      5 5 5
#
