__author__ = 'robinjayaswal'

import inverseMatrix
import matrixAddition
import matrixMultiplication
import printMatrix
import rowReduceAugmented
import matrixTranspose


def main():
    matrix1 = [[1, 2, 3], [5, 6, 7], [9, 2, 5]]
    matrix2 = [[10, 10, 10], [1, 2, 1], [5, 5, 5]]
    matrix3 = [[1], [1], [5]]

    print("Matrix one is:\n")
    printMatrix.printMatrix(matrix1)

    print("Matrix two is:\n")
    printMatrix.printMatrix(matrix2)

    print("Matrix three is:\n")
    printMatrix.printMatrix(matrix3)

    print("________________________")
    print("")
    print("TESTING MATRIX ADDITION")

    print("Matrix one plus matrix two should give:\n")

    sumCorrectAnswer = [[11, 12, 13], [6, 8, 8], [14, 7, 10]]

    printMatrix.printMatrix(sumCorrectAnswer)

    print("")

    print("calling addMatrices(matrix1, matrix2) gives")

    print("")
    additionResult = matrixAddition.addMatrices(matrix1, matrix2)

    printMatrix.printMatrix(additionResult)

    if (additionResult == sumCorrectAnswer):
        print("SUCCESS")
    else:
        print("FAILURE")
        return

    print("")
    print("_________________________")
    print("")

    print("TESTING MATRIX MULTIPLICATION")

    print("Matrix one times matrix three should give:\n")

    productCorrectAnswer = [[18], [46], [36]]

    printMatrix.printMatrix(productCorrectAnswer)

    print("calling multiplyMatrices(matrix1, matrix3) gives")

    print("")
    multiplyResult = matrixMultiplication.multiplyMatrices(matrix1, matrix3)

    printMatrix.printMatrix(multiplyResult)

    if (multiplyResult == productCorrectAnswer):
        print("SUCCESS")
    else:
        print("FAILURE")
        return

    print("")
    print("_________________________")
    print("")

    print("TESTING MATRIX INVERSION")

    print("Inverse of matrix one should give:\n")

    inverseCorrectAnswer = [[-.4, .1, .1], [-.95, .55, -.2], [1.1, -.4, .1]]

    printMatrix.printMatrix(inverseCorrectAnswer)

    print("calling getInverseMatrix(matrix1) gives")

    print("")
    inverseResult = inverseMatrix.getInverseMatrix(matrix1)
    printMatrix.printMatrix(inverseResult)

    if (multiplyResult == productCorrectAnswer):
        print("SUCCESS")
    else:
        print("FAILURE")
        return


    print("")
    print("_________________________")
    print("")

    print("TESTING MATRIX TRANSPOSE")

    print("Transpose of matrix 3 should be:\n")



    transposeCorrectAnswer = [[1, 1, 5]]

    printMatrix.printMatrix(transposeCorrectAnswer)

    print("calling matrixTranspose(matrix3) gives")

    print("")
    transposeResult = matrixTranspose.matrixTranspose(matrix3)
    printMatrix.printMatrix(transposeResult)

    if (transposeResult == transposeCorrectAnswer):
        print("SUCCESS")
    else:
        print("FAILURE")
        return


    print("")
    print("_________________________")
    print("")

    print("TESTING AUGMENTED MATRIX ROW REDUCTION")

    augmentedMatrix = [[1, 2, 3, 2], [5, 6, 7, 5], [9, 2, 5, 2]]

    print("Augmented Matrix One is: ")

    printMatrix.printMatrix(augmentedMatrix)

    print("")

    print("Echelon row reduced form of matrix 2:\n")

    printMatrix.printMatrix(rowReduceAugmented.rowReduceAugmented(augmentedMatrix))




main()
