def bitIntertion(n,m,i,j):
    """
    clear bit from i to j in n
    shift m i bits
    merge m and n
    """
    allOne = ~0
    right = allOne << (j+1)
    left = (1 << 2) -1
    mask = right | left
    n_cleared = n & mask
    m_shifted = m << i
    print(bin(n_cleared|m_shifted))
n = 0b10000000000
m = 0b10011
i = 2
j = 6
bitIntertion(n,m,i,j)