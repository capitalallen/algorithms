def printBinary(n):
    print("printBinary(" +str(n) +")")
    if n >1:
        print(n)
        printBinary(n//2)
    print(n%2,end='')

n = 43
printBinary(n)