# 01 KNAPSACK PROBLEM
def sort(weight, profit, n):
    swapped = False
    for i in range(n):
        for j in range(n-1):
            if weight[j] > weight[j+1]:
                swapped = True
                weight[j], weight[j+1] = weight[j+1], weight[j]
                profit[j], profit[j+1] = profit[j+1], profit[j]
        if not swapped:
            break 
    return weight, profit

def show(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            print(matrix[i][j], end="\t")
        print("\n")


def knap01(weight, profit, capacity, n):
    ks = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= weight[i-1]:
                ks[i][j] = max(ks[i-1][j], ks[i-1][j-weight[i-1]] + profit[i-1])
            else:
                ks[i][j] = ks[i-1][j]

    show(ks)
    return ks[n][capacity]

weight = []
profit = []
n = int(input("\nEnter the no of knapsack elements : "))
for i in range (n):
    w, p = map(int, input(f"\nEnter the weight and profit for item {i + 1} separated by space: ").split())
    weight.append(w)
    profit.append(p)

capacity = int(input("\nEnter the capacity of Knapsack: "))
n = len(weight)

weight, profit = sort(weight, profit, n)
print(f"\nMaximum Profit = {knap01(weight, profit, capacity, n)}")