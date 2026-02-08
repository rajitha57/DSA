# Given string
s = "CSIPLEARNING"
# Convert string to list (strings are immutable)
L = list(s)
n = len(L)
# Bubble sort for descending order
for i in range(n):
 for j in range(0, n - i - 1):
  if L[j] < L[j + 1]:   # change sign for descending
    L[j], L[j + 1] = L[j + 1], L[j]
# Convert back to string
sorted_string = "".join(L)
print("Alphabets in descending order:", sorted_string)

