'''In this method,We take two inputs,a matrix of coefficients of variables
and a matrix of right hand side coefficients.
Calculate a determinant of the main (square) matrix.
To find the 'i'th solution of the system of linear equations using
Cramer's rule replace the 'i'th column of the main matrix by solution
vector and calculate its determinant. Then divide this determinant by
the main one - this is one part of the solution set, determined using
Cramer's rule. Repeat this operation for each variable.
For determinant calculation,we use gaussian elimination method.'''
import copy
def findDeterminant(m):
    ans = []
    for row in range(len(m)):
        for col in range(len(m[0])):
            if row == col:
                pe = m[row][col]
                ans.append(pe)  # Stores the diagonal elements
                if pe != 0:
                    for r in range(len(m[0])):
                        m[row][r] = round(m[row][r] / pe, 3)
                    for j in range(len(m)):
                        if j > row:
                            makeZero = m[j][col]
                            for k in range(len(m[0])):
                                m[j][k] = round(m[j][k] - m[row][k] * makeZero, 3)
    result = 1
    for r in range(len(ans)):
        result *= ans[r]
    return round(result)

def cramerRule():
    matrixDimension = int(input('Enter the dimension of matrix:'))
    matrix = [] # This is the matrix of coefficients on the left hand side
    for i in range(matrixDimension):
        row = []
        for j in range(matrixDimension):
            number = float(input(f"Enter the number for row {i + 1} and column {j + 1}:"))
            row.append(number)
        matrix.append(row)
    # This is the matrix of coefficients of right hand side
    constants = []
    for i in range(matrixDimension):
        number = int(input('Enter the right hand side coefficients one by one:'))
        constants.append(number)
    # Making a copy of main matrix because the original matrix
    # will get change after finding its determinant
    copyMatrix = copy.deepcopy(matrix)
    # Here,we are calculating the determinant of main matrix
    det = findDeterminant(matrix)
    # It the matrix is singular
    if det == 0:
        print("The solution of this system doesn't exist.")
    else: # If the matrix is non-singular
        for i in range(matrixDimension):
            newMatrix = [] # This is the new matrix after changing the column with right hand side coefficients
            for j in range(len(copyMatrix)):
                row = []
                for k in range(len(copyMatrix[0])):
                    if k == i:
                       row.append(constants[j])
                    else:
                       row.append(copyMatrix[j][k])
                newMatrix.append(row)
            # determinant of new matrix
            detOfNewMatrix = findDeterminant(newMatrix)
            ans = round((detOfNewMatrix / det), 3)
            print(f"x{i + 1} = {ans}")
cramerRule()
