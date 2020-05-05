# bottom-up dp solution
# return max revenue
def rc(n,p):
    r=[i for i in range(0,n+1)]
    r[0] = 0 
    for j in range(1,n+1):
        q = float('-inf')
        for i in range(j):
            q = max(q,p[i]+r[j-i-1])
        r[j] = q 
    return r[n]

def rc_detail(n,p):
    r=[i for i in range(0,n+1)]
    s=[i for i in range(0,n+1)]
    r[0] = 0 
    for j in range(1,n+1):
        q = float('-inf')
        for i in range(j):
            if q<p[i]+r[j-i-1]:
                q = max(q,p[i]+r[j-i-1])
                s[j] = i+1 
        r[j] = q 
    return (r,s)

def print_result(n,p):
    r,s = rc_detail(n,p)
    while n>0:
        print(s[n])
        n = n-s[n]
arr = [1, 5, 8, 9, 10, 17, 17, 20] 
size = len(arr) 
print(print_result(size,arr))
print(rc_detail(size,arr))
