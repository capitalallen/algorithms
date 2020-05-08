def flipbit(num):
    """
    input: int
    output: int max 1s
    c: optimze
    e: num == 0
    """
    if (~num) == 0:
        return len(bin(num)[2:])
    a = num
    currLen = 0
    prevLen = 0
    maxLen = 0
    while a > 0:
        """
        check 
            a&1 == 1: currLen +=1
            a&1 == 0: if a&2 ==0 --> prevLen =0 else prevLen = currLen then currLen = 0
            max (currLen+prevLen,currLen)
            a shift right by 1
        return maxLen + 1
        """
        if (a&1) == 1:
            currLen +=1
        elif (a&1) ==0:
            if (a&2) == 0:
                prevLen =0
            else:
                prevLen = currLen
            currLen = 0
        maxLen = max(currLen+prevLen,currLen)
        a >>= 1
    return maxLen+1
# Driver code 
# input 1 
print(flipbit(13)); 
  
# input 2 
print(flipbit(1775)); 
  
# input 3 
print(flipbit(15)); 