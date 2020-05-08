def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount == 0:
        return 0
    value1 = [0]
    value2 = []
    nc =  0
    visited = [False]*(amount+1)
    visited[0] = True
    while value1:
        nc += 1
        for v in value1:
            for coin in coins:
                newval = v + coin
                print('')
                print('newval: ',newval,'value1:',value1,'coin: ',coin)
                print('visited:',visited)
                if newval == amount:
                    return nc
                elif newval > amount:
                    continue
                elif not visited[newval]:
                    visited[newval] = True
                    value2.append(newval)
        value1, value2 = value2, []
    return -1

coins = [1,2,5]
amount = 11
print(coinChange(coins,amount))