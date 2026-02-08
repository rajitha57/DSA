#bubble sort
# Given list
L = [64, 34, 25, 12, 22, 11, 90]
n = len(L)
for i in range(n):
    for j in range(0, n - i - 1):
        if L[j] > L[j + 1]:
            # swap
            L[j], L[j + 1] = L[j + 1], L[j]
print("Sorted list in ascending order:", L)

