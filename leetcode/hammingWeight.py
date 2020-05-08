def hammingWeight(n):
    return bin(int(n)).count('1')


a = bin(5)
print(a[2:])
print(hammingWeight(a[2:]))
