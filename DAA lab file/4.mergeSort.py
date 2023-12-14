# IMPLEMENTATION OF MERGE SORT 

def merge(arr, l, q, r):
    n1 = q - l + 1
    n2 = r - q

    L1 = [0] * (n1 + 1)
    L2 = [0] * (n2 + 1)

    for i in range(n1):
        L1[i] = arr[l + i]

    for j in range(n2):
        L2[j] = arr[q + j + 1]

    L1[n1] = float('inf')
    L2[n2] = float('inf')

    i = j = 0

    for k in range(l, r + 1):
        if L1[i] <= L2[j]:
            arr[k] = L1[i]
            i += 1
        else:
            arr[k] = L2[j]
            j += 1

def mergeSort(arr, p, r):
    if p < r:
        m = p + (r - p) // 2

        mergeSort(arr, p, m)
        mergeSort(arr, m + 1, r)
        merge(arr, p, m, r)

arr = []
n = int(input("Enter the number of elements in the array: "))
for i in range(n):
    arr.append(int(input(f"Enter the {i + 1} element: ")))

mergeSort(arr, 0, n - 1)
print(f"Array after Merge Sort: {arr}")
