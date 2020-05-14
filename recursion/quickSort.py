def quicksort(arr):
    n = len(arr)
    qsort(arr,0,n-1)
def qsort(arr,l,h):
    if l < h:
        p = partition(arr,l,h)
        qsort(arr,l,p-1)
        qsort(arr,p+1,h)
    
def partition(arr,l,h):
    # (4,2,9,5,6)
    pivot = arr[h]
    i = l 
    for j in range(l,h):
        if arr[j]<pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[i],arr[h] = arr[h],arr[i]
    return i 
