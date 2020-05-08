
def bitSwapRequired(a, b):
    # write your code here
    """
    count = 0
    convert n to bin value with [2:]
    convert m to bin value with [2:]
    for loop compare n[i] with m[i]
        if different count +1 
    """
    big = bin(a)[2:] if a >= b else bin(b)[2:]
    small = bin(b)[2:] if b < a else bin(a)[2:]
    small = "0"*(len(big)-len(small))+small 
    count = 0
    print(big,small)
    for i in range(len(big)):
        if big[i] != small[i]:
            count +=1 
        
    return count
a= 31
b = 14
print(bitSwapRequired(a,b))