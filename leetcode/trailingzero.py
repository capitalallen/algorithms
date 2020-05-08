def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
        count =0
        total =1
        for i in range(1,n+1):
            total *=i 
        total = str(total)
        print(total)
        i = len(total)-1
        while i>0:
            if total[i] == '0':
                count +=1 
                i -=1
            else:
                return count
n = 11
print(trailingZeros(n))
            
            