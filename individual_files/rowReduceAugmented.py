import printMatrix
__author__ = 'robinjayaswal'

def rowReduceAugmented(augmentedMatrix):
    # if there are too few variables, do not even bother
    if (len(augmentedMatrix) < len(augmentedMatrix[0]) - 1):
        print("Too few rows, cannot reach echelon form")
        return None

    # create copy of matrix so as not to change matrix given to us
    reducedEchelonMatrix = list(augmentedMatrix)

    # going down step.
    for i in range(len(augmentedMatrix)):
        main = reducedEchelonMatrix[i][i]   # store the diagonal we are currently working with
        for j in range(i + 1, len(augmentedMatrix)):    # go down column to make every entry zero
            divisor = float(main) / float(reducedEchelonMatrix[j][i])
            for k in range(i, len(augmentedMatrix[0])):
                # multiply entire row of the current entry we are eliminating by the factor, subtract corresponding entry
                # of the main row
                reducedEchelonMatrix[j][k] *= divisor
                reducedEchelonMatrix[j][k] -= reducedEchelonMatrix[i][k]

    # going up step
    for i in range(len(augmentedMatrix)):
        # calculate current row and column of the main diagonal we will use to eliminate above entries
        row = len(augmentedMatrix) - 1 - i
        column = len(augmentedMatrix[0]) - 2 - i
        main = reducedEchelonMatrix[row][column]
        for j in range(0, row): # go through all rows above the current main diagonal to make column above all 0's
            divisor = float(main) / float(reducedEchelonMatrix[j][column])

            pivot = reducedEchelonMatrix[j][j]
            pivot *= divisor
            pivot -= reducedEchelonMatrix[row][j]

            pivotScalar = 1.0 / pivot

            for k in range(0, len(augmentedMatrix[0])):  # go through entire current row multiplying by factor and subtracting
                reducedEchelonMatrix[j][k] *= divisor
                reducedEchelonMatrix[j][k] -= reducedEchelonMatrix[row][k]

                reducedEchelonMatrix[j][k] *= pivotScalar

                # round the matrix entry to 3 decimal places
                reducedEchelonMatrix[j][k] = float("{0:.3f}".format(reducedEchelonMatrix[j][k]))

    # finally, round the bottom row to 3 decimal places since it never got rounded above like the others
    lastRow = len(reducedEchelonMatrix) - 1
    pivotScalar = 1.0 / reducedEchelonMatrix[lastRow][lastRow]

    for i in range(len(reducedEchelonMatrix[0])):
        reducedEchelonMatrix[lastRow][i] *= pivotScalar
        reducedEchelonMatrix[lastRow][i] = float("{0:.3f}".format(reducedEchelonMatrix[lastRow][i]))

    return reducedEchelonMatrix


# matrix:
# 1 2 3 | 2
# 5 6 7 | 5
# 9 2 5 | 2
# .2 * 6 = 1.2, 1.2 - 2

matrix1 = [[1, 2, 3, 2], [5, 6, 7, 5], [9, 2, 5, 2]]
printMatrix.printMatrix(rowReduceAugmented(matrix1))