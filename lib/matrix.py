__author__ = 'robinjayaswal'


def getInverseMatrix(matrix):
    # if there are too few variables, do not even bother
    if (len(matrix) != len(matrix[0])):
        print(str(len(matrix)) + " x " + str(len(matrix[0])) + " is not invertible. Must be n x n")
        return None

    # create copy of matrix so as not to change matrix given to us
    tempReducingMatrix = list(matrix)

    # create an identity matrix we will turn into inverse matrix by turning matrix into identity
    inverse = []
    for i in (range(len(matrix))):
        inverse.append([])
        for j in range(len(matrix[0])):
            if (i == j):
                inverse[i].append(1)
            else:
                inverse[i].append(0)

    # going down step.
    for i in range(len(matrix)):
        main = tempReducingMatrix[i][i]   # store the diagonal we are currently working with
        for j in range(i + 1, len(matrix)):    # go down column to make every entry zero
            divisor = float(main) / float(tempReducingMatrix[j][i])
            for k in range(0, len(matrix[0])):
                # multiply entire row of the current entry we are eliminating by the factor, subtract corresponding entry
                # of the main row
                tempReducingMatrix[j][k] *= divisor
                tempReducingMatrix[j][k] -= tempReducingMatrix[i][k]

                # perform same row operation on the identity matrix to turn into inverse
                inverse[j][k] *= divisor
                inverse[j][k] -= inverse[i][k]


    # going up step
    for i in range(len(matrix)):
        # calculate current row and column of the main diagonal we will use to eliminate above entries
        row = len(matrix) - 1 - i
        column = len(matrix[0]) - 1 - i
        main = tempReducingMatrix[row][column]
        for j in range(0, row): # go through all rows above the current main diagonal to make column above all 0's
            divisor = float(main) / float(tempReducingMatrix[j][column])

            # calculate the number we will scale the current row by after eliminating entry to make pivot '1'
            pivot = tempReducingMatrix[j][j]
            pivot *= divisor
            pivot -= tempReducingMatrix[row][j]

            pivotScalar = 1.0 / pivot

            for k in range(0, len(tempReducingMatrix[0])):  # go through entire current row multiplying by factor and subtracting
                tempReducingMatrix[j][k] *= divisor
                tempReducingMatrix[j][k] -= tempReducingMatrix[row][k]

                # scale by the factor needed to make pivot 1
                tempReducingMatrix[j][k] *= pivotScalar

                # round the matrix entry to 3 decimal places
                tempReducingMatrix[j][k] = float("{0:.3f}".format(tempReducingMatrix[j][k]))

                # perform same operation on the identity matrix to turn it into inverse
                inverse[j][k] *= divisor
                inverse[j][k] -= inverse[row][k]
                inverse[j][k] *= pivotScalar

                inverse[j][k] = float("{0:.3f}".format(inverse[j][k]))

    # finally, round the bottom row to 3 decimal places since it never got rounded above like the others
    lastRow = len(tempReducingMatrix) - 1
    pivotScalar = 1.0 / tempReducingMatrix[lastRow][lastRow]

    for i in range(len(tempReducingMatrix[0])):
        tempReducingMatrix[lastRow][i] *= pivotScalar
        tempReducingMatrix[lastRow][i] = float("{0:.3f}".format(tempReducingMatrix[lastRow][i]))

        inverse[lastRow][i] *= pivotScalar
        inverse[lastRow][i] = float("{0:.3f}".format(inverse[lastRow][i]))

    return inverse


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


def matrixTranspose(matrix):
    transposedMatrix = []
    for j in range(len(matrix[0])):
        transposedMatrix.append([])
        for i in range(len(matrix)):
            transposedMatrix[j].append(matrix[i][j])

    return transposedMatrix


def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # print("", matrix[i][j])
            print(repr(matrix[i][j]).rjust(5)),

            if (j == len(matrix[0]) - 1):
                print("\n")



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


