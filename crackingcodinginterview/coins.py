def makeChange(amount,denoms,index):
    if index >= len(denoms) -1:
        return 1
    denomAmount = denoms[index]
    ways =0
    i = 0
    while i*denomAmount <= amount:
        amountRemining = amount -i*denomAmount
        ways += makeChange(amountRemining,denoms,index+1)

def callChange(n):
    denoms = (25,10,5,1)
    return makeChange(n,denoms,0)

a = callChange(10)
print(a)