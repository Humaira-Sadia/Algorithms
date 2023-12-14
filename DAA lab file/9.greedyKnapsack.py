# GREEDY KNAPSACK OR FRACTIONAL KNAPSACK 

def knapsack(ratio, profit, weight, W):
    n = len(ratio)
    
    for i in range(n):
        ratio[i] = profit[i] / weight[i]

    for i in range(n):
        for j in range(n):
            if ratio[j] > ratio[i]:
                ratio[i], ratio[j] = ratio[j], ratio[i]
                profit[i], profit[j] = profit[j], profit[i]
                weight[i], weight[j] = weight[j], weight[i]
    
    print("Sorted items :\n Id \t Profit \t Weight \t Ratio")
    for i in range(n):
        print(f"{i+1} \t {profit[i]} \t {weight[i]} \t {ratio[i]}")

    total_profit = 0
    for i in range(n):
        if weight[i] <= W:
            W -= weight[i]
            total_profit += profit[i]
        else:
            fraction = W / weight[i]
            total_profit += profit[i] * fraction
            break

    print("\nTotal profit in Knapsack:", total_profit)

n = int(input("Enter the no of objects : "))
W = int(input("Enter maximum capacity of bag : "))
profit = [int(x) for x in input("Enter profits as space separated values : ").split()]
weight = [int(x) for x in input("Enter corresponding weights as space separated values : ").split()]
ratio = [0] * n  
print(ratio)

print("\nItems included in Knapsack are : ")
knapsack(ratio, profit, weight, W)

