def bubble_sort(l):
  for i in range(len(l)):
      for j in range(i+1,len(l)):
          if l[i]>l[j]:
              l[i],l[j]=l[j],l[i]
  return l



print(bubble_sort([4,2,6,5,1,3]))



"""
  EXPECTED OUTPUT:
  ----------------
  [1, 2, 3, 4, 5, 6]

"""


