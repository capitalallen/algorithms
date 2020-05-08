def updateBits(n, m, i, j):
    # write your code here
    """
    clean bit between i to j from N 
    add i numbers of zeros to end of M 
    N = N or M 
    """
    print('n,''{:032b}'.format(n))
    clean = int('0b'+'1'*(32-j)+'0'*(j-i)+'1'*i,2)
    print(clean,'{:032b}'.format(clean))
    n = n&clean 
    print('{:032b}'.format(n))
    m = '0b'+bin(m)[2:]+'0'*i 
    print('{:032b}'.format(int(m,2)))
    return n|int(m,2) 

n = int('0b10000000000',2)
m = int('0b10101',2)
i =2 
j =6
a = updateBits(n,m,i,j)
print('{:032b}'.format(a))
    