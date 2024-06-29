""" 
  Same as bubble sort but need index look at first item.
  Keep track of index with minimum value
"""
def selection_sort(l):
    min_index=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[j]<l[min_index]:
                min_index=j 
        l[i],l[min_index]=l[min_index],l[i]
        min_index=i+1
    return l

print(selection_sort([4,2,6,5,1,3]))
