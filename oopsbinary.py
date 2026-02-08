class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, key):
        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == key:
                return mid
            elif self.arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1
        return -1
# Main program
arr = [10, 20, 30, 40, 50, 60]
key = int(input("enter any key: "))
obj = BinarySearch(arr)
result = obj.search(key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
