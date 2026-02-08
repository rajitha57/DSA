#creation of class and object
# class greeting:
#     def hello(self):
#         print("welcome to DSA")
# x=greeting()
# x.hello()

#linear search
def linear_search(a, key, n): 
    for i in range(n): 
     if a[i] == key:
      return i  
    return -1 
a = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29] 
key=int(input("Enter key:"))
n = len(a) 
result = linear_search(a, key, n) 
if(result == -1): 
    print("Element not found") 
else: 
    print("Element found at index: ", result)


