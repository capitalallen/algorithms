def searchRange(A, target):
    # write your code here
    """
        0, 1, 2, 3, 4, 5
    [5, 7, 7, 8, 8, 10]
    output [3,4]
    """
    l,r = 0,len(A)-1
    output = []
    if r +1 == 0:
        return [-1,-1]
    while l<=r:
        m = int((l+r)/2)
        if A[m]==target:
            tmp = m
            output.append(m)
            while 0<tmp and A[tmp-1] == target:
                tmp -=1
                output.append(tmp)
            while tmp+1<len(A) and A[tmp+1]==target:
                tmp += 1
                output.append(tmp)
            return [min(output),max(output)]
        elif A[m] >target:
            r = m -1 
        else:
            l = m + 1 
    return [-1,-1]
A = [1]
target = 1
print(searchRange(A,target))