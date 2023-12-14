# BINARY SEARCH
def binarySearch(arr, low, high, target):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, low, mid - 1, target)
        else:
            return binarySearch(arr, mid + 1, high, target)
    else: 
        return -1

arr = []
n = int(input("Enter the number of elements in the array : "))
for i in range(n):
    arr.append(int(input(f"Enter the {i+1} element : ")))

target = int(input("Enter the target value : "))

result = binarySearch(arr, 0, n-1, target)

if(result == -1): 
    print("Target element not found in the array")
else:
    print(f"Target element {target} found at index {result} of the array.")