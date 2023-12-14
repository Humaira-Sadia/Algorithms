# IMPLEMENTATION OF HEAP SORT 

def max_heapify(arr, n, i):
    lc = i*2+1
    rc = i*2+2
    largest = i

    if lc < n and arr[lc] > arr[largest]:
        largest = lc

    if rc < n and arr[rc] > arr[largest]:
        largest = rc

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heapSort(arr, n):
    for i in range (n):
        max_heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr,i,0)

arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input(f"Enter the {i + 1} element: ")))

heapSort(arr, n)
print(f"The sorted array is: {arr}")
