__author__ = 'robinjayaswal'

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print("", matrix[i][j])
            print(repr(matrix[i][j]).rjust(5)),

            if (j == len(matrix[0]) - 1):
                print("\n")



# matrix2 = [[10, 10, 10], [1, 2, 1], [5, 5, 5]]
# printMatrix(matrix2)