def findCommon(x,y):
    result = []
    j = 0
    k = 0
    for i in range(len(x)):
        j = k
        while j < len(y):
            if x[i] == y[j]:
                result.append(x[i])
                k = i
            j +=1
    return result



x = [13,27,35,40,49,55,59]
y = [17,35,39,40,55,58,60]
print(findCommon(x,y))