"""
[1,3,5,6], 5 → 2
A,target,s,e,answer=3
m = (s+e)//2
"""
def search(A,target):
    s=0
    e=len(A)-1
    answer = e-1
    return searchposition(A,target,s,e,answer)
def searchposition(A,target,s,e,answer):
    m = int((s+e)/2)
    if s<=e:
        if A[m]<=A[answer]:
            print(m)
            answer = m
        if A[m] > A[answer]:
            return searchposition(A,target,s,m-1,answer)
        elif A[m] < A[answer]:
            return searchposition(A,target,m+1,e,answer)
        else:
            return answer 
    else:
        return answer

A= [1,3,5,6]
target = 2
a = search(A,target)
print(a)