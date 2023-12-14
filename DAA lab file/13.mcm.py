# MATRIX CHAIN MULTIPLICATION
def show(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(cols):
            print(matrix[i][j], end="\t")
        print("\n")

def mcm(p, n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf') 
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q

    show(m) 
    return m[1][n - 1]

p = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    p.append(int(input("Enter the element: ")))
print(mcm(p, 5))

