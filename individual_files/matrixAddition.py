__author__ = 'robinjayaswal'

def addMatrices(matrix1, matrix2):
    if ( (len(matrix1) != len(matrix2)) or (len(matrix1[0]) != len(matrix2[0]))):
        print("Matrix dimensions must match: Cannot add " + len(matrix1) + "x" +len(matrix1[0]) + " and " + len(matrix2) + "x" + len(matrix2[0]))
        return

    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix1[0])):
            result[i].append(matrix1[i][j] + matrix2[i][j])

    return result


# matrix1 = [[1, 2, 3], [5, 6, 7], [9, 2, 5]]
# matrix2 = [[10, 10, 10], [1, 1, 1], [5, 5, 5]]
#
# print(addMatrices(matrix1, matrix2))