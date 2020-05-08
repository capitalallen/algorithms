def perm2(A, k):
    r = [[]]
    for i in range(len(A)):
        r = [[a] + b for a in A for b in r if a not in b]
    return r

A,k = [1,2,3],2
print(perm2(A,k))