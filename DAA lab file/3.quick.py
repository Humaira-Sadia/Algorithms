# QUICK SORT IMPLEMENTATION
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pidx = partition(arr, low, high)

        quickSort(arr, low, pidx - 1)
        quickSort(arr, pidx + 1, high)

arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input(f"Enter the {i + 1} element: ")))

quickSort(arr, 0, n - 1)
print(f"Array after Quick Sort: {arr}")
