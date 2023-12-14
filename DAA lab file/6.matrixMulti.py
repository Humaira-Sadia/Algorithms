# SIMPLE MATRIX MULTIPLICATION
row1=0; row2=0; col1=0; col2 = 0

def show(arr, row, col):
    for i in range(row):
        for j in range(col):
            print(arr[i][j], end='\t')
        print("")

def multiply(arr1, arr2):
    res = [[None] * col2 for i in range(row1)]
    for i in range(row1):
        for j in range(col2):
            res[i][j] = 0
            for k in range(row2):
                res[i][j] += arr1[i][k] * arr2[k][j]
    print("\n*** After Matriz Multiplication ***\n")
    show(res, row1, col2)

def addElems(arr, row, col):
    print("Enter the elements in the array:")
    for i in range(row):
        for j in range(col):
            arr[i][j] = int(input())
    print("*** Matrix ***\n")
    show(arr, row, col)

row1 = int(input("Enter the number of rows of Array-1: "))
col1 = int(input("Enter the number of columns of Array-1: "))
arr1 = [[0]*col1 for i in range (row1)]
addElems(arr1, row1, col1)

row2 = int(input("Enter the number of rows of Array-2: "))
col2 = int(input("Enter the number of columns of Array-2: "))
arr2 = [[0]*col2 for i in range (row2)]
addElems(arr2, row2, col2)

multiply(arr1, arr2)