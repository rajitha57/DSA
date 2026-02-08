def mergesort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    lefthalf=a[:mid]
    righthalf=a[mid:]
    sortedleft=mergesort(lefthalf)
    sortedright=mergesort(righthalf)
    return merge(sortedleft, sortedright)
def merge(left, right):
    result=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i=i+1
        else:
            result.append(right[j])
            j=j+1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
a=[70,20,10,90,40,30]
print("list aftersorting:", mergesort(a))

    