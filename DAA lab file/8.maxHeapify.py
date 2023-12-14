# MAX HEAPIFY IMPLEMENTATION
def max_heapify(arr, n, i):
    largest = i
    lc = 2*i+1
    rc = 2*i+2

    if lc < n and arr[lc] > arr[largest] :
        largest = lc

    if rc < n and arr[rc] > arr[largest] :
        largest = rc

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


def create_max_heapify(arr, n):
    start = n//2 - 1
    for i in range(start, -1, -1):
        max_heapify(arr, n, i)
    print(arr)


def insert(arr, n, key):
    arr.append(key)
    n = n+1
    print(f"\nAfter inserting the key : \nMax Heap :")
    create_max_heapify(arr, n)

def increase_key(arr, n, key, value):
    flag = -1
    for i in range(n):
        if arr[i] == key:
            flag = i
            break
    if flag == -1:
        print("\nThe given key is not present in the array\n")
        return -1
    arr[i] = arr[i] + value
    print(f"\nAfter increasing the {key} with {value}\n Max heap :")
    create_max_heapify(arr, n)

def decrease_key(arr, n, key, value):
    flag = -1
    for i in range(n):
        if arr[i] == key:
            flag = i
            break
        if flag == -1:
            print("\nThe given key is not present in the array\n")
            return -1
    arr[i] = arr[i] - value
    print(f"\nAfter decreasing the {key} with {value}\n Max heap :")
    create_max_heapify(arr, n)

def extract_max(arr, n):
    max = arr[0]
    print(f"\nMaximum element after extracting : {max}\n")
    arr[0] = arr[n-1]
    n = n-1
    print("\nMax heap : \t")
    create_max_heapify(arr,n)

arr = [15, 19, 5, 8, 10, 20, 12, 9, 11, 3]
n = len(arr)

create_max_heapify(arr, n)
insert(arr,n,33)
increase_key(arr, n, 5,12)
decrease_key(arr, n, 9,4)
extract_max(arr,n)
