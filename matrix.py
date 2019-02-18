"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    output = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            output += str(matrix[j][i]) + ' '
        output += '\n' if i != len(matrix) - 1 else ''
    print(output)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(i == j):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    res = []
    for row in m1:
        new = []
        for i in range(len(m2[0])):
            sum = 0
            for j in range(len(row)):
                sum += row[j] * m2[j][i]
            new.append(sum)
        res.append(new)
    
    for i in range(len(m2)):
        for j in range(len(m2[0])):
            m2[i][j] = res[i][j]

    # print(m2)



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

# print('------------------')
# arr = new_matrix()
# ident(arr)
# print_matrix(arr)
# print('------------------')

m2 = [[1, 4], [2, 5], [3, 6], [1, 1]]
m1 = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12], [1, 1, 1, 1]]
matrix_mult(m1, m2)

