def selection_sort(a,n):
 for i in range(n):
  min=i
  for j in range(i+1, n):
   if a[j]<a[min]:
    min=j
  a[i], a[min]=a[min], a[i]
 return a
a=[9,8,7,6,5,4,3] 
n=len(a)
print("list after sorting: ", selection_sort(a,n) ) 
    