#using list comprehension
def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    left = [x for x in a[1:] if x <= pivot]
    right = [x for x in a[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = quick_sort(a)
print(a)

# Using for loop instead of list comprehension
def quick_sort(a):
    if len(a) <= 1:
        return a

    pivot = a[0]
    left = []
    right = []    
    for x in a[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)
a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
a = quick_sort(a)
print(a)
