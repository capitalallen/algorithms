import math
def magicIndex(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return arr[i]
    return False
def magicIndexB(arr):
    return helper(arr,0,len(arr)-1)
def helper(arr,start,end):
    if end < start:
        return -1
    middle = math.floor((end+start)/2)
    print(middle)
    if arr[middle] == middle:
        return middle 
    elif arr[middle] > middle:
        return helper(arr,start,middle-1)
    else:
        return helper(arr,middle+1,end)
arr = [-1,0,1,2,4,5]
a = magicIndex(arr)
b = magicIndexB(arr)
print(a)
print(b)
"""
-101245
0 12345
"""
