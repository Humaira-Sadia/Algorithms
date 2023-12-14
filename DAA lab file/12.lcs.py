# LONGEST COMMOM SUBSEQUENCE
def show(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(cols):
            print(matrix[i][j], end="\t")
        print("\n")

def print_lcs(X, Y, Z, m, n):
    if m == 0 or n == 0:
        return ['']
    if X[m-1] == Y[n-1]: 
        sub = print_lcs(X, Y, Z, m-1, n-1)
        for i in range(len(sub)):
            sub[i] += X[m-1]
        return sub
    if Z[m][n-1] > Z[m-1][n]:
        return print_lcs(X, Y, Z, m, n-1)
    if Z[m][n-1] < Z[m-1][n]:
        return print_lcs(X, Y, Z, m-1, n)
    top = print_lcs(X, Y, Z, m-1, n)
    left = print_lcs(X, Y, Z, m, n-1)

    return top + left


def lcs_find(X, Y, m, n):
    Z = [[None] * (n+1) for i in range (m+1)]

    for i in range (m+1):
        for j in range (n+1):
            if i == 0 or j == 0: 
                Z[i][j] = 0
            elif X[i-1] == Y[j-1]:
                Z[i][j] = 1 + Z[i-1][j-1]
            else:
                Z[i][j] = max(Z[i][j-1], Z[i-1][j])
    show(Z)
    print(f"All Possible Subsequences : {print_lcs(X, Y, Z, m, n)}")
    return Z[m][n]

X = int(input("Enter the 1st String : "))
Y = int(input("Enter the 2nd String : "))
m = len(X)
n = len(Y)

length = lcs_find(X, Y, m, n)
print(f"Length of Longest Common Subsequence : {length}")
