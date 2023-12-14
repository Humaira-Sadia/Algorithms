
import numpy as np
def addElems(arr, row, col):
    print("Enter the elements in the array:")
    for i in range(row):
        for j in range(col):
            arr[i][j] = int(input())
    print("*** Matrix ***\n")
    show(arr, row, col)
def show(arr, row, col):
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end='\t')
        print("")

def split(matrix):
	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):

	if len(x) == 1:
		return x * y

	a, b, c, d = split(x)
	e, f, g, h = split(y)

	p1 = strassen(a, f - h) 
	p2 = strassen(a + b, h)	 
	p3 = strassen(c + d, e)	 
	p4 = strassen(d, g - e)	 
	p5 = strassen(a + d, e + h)	 
	p6 = strassen(b - d, g + h) 
	p7 = strassen(a - c, e + f) 

	c11 = p5 + p4 - p2 + p6 
	c12 = p1 + p2		 
	c21 = p3 + p4		 
	c22 = p1 + p5 - p3 - p7 

	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22)))) 

	return c

row1 = int(input("Enter the number of rows of Array-1: "))
col1 = int(input("Enter the number of columns of Array-1: "))
arr1 = [[0]*col1 for i in range (row1)]
addElems(arr1, row1, col1)

row2 = int(input("Enter the number of rows of Array-2: "))
col2 = int(input("Enter the number of columns of Array-2: "))
arr2 = [[0]*col2 for i in range (row2)]
addElems(arr2, row2, col2)

C = strassen(np.array(arr1), np.array(arr2))
print("\n*** Matrix After Multiplication ***\n")
show(C, row1, col2)