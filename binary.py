#binary search
def binary_search(a, key):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if key == a[mid]:
            return mid
        elif key > a[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
a = [19, 28, 37, 46, 55, 64, 73]
key = int(input("Enter key: "))
result = binary_search(a, key)
if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)
