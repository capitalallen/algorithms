def indent(n):
    for i in range(n):
        print("    ")

def permuteHelper(a, l, r):
    if l == r:
        print (''.join(a)) 
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permuteHelper(a, l + 1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 

# def permute(s):
#     permuteHelper(s,'')

string = "ABC"
n = len(string) 
a = list(string) 
permuteHelper(a, 0, n-1) 