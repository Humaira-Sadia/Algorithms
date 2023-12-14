# INSERTION SORT ALGO IMPLEMENTATION
def insertion(arr, n):
    for j in range (1,n):
        key = arr[j]
        i = j-1
        while i >= 0 and key < arr[i]:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key
    print(arr)
    return

arr = []
n = int(input("Enter the number of elements in the array : "))
for i in range(n):
    arr.append(int(input(f"Enter the {i+1} element : ")))

insertion(arr, n)