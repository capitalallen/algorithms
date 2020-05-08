def generateMatrix(n: int):
    x = 1
    output = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            output[i].append(x)
            x +=1
    return output