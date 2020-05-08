def generateMatrix(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        print('before',i,j,di,dj)
        if A[(i+di)%n][(j+dj)%n]:
            print(i,j,di,dj)
            di, dj = dj, -di
            print('after',i,j,di,dj)
        i += di
        j += dj
    return A

n = 3
a = generateMatrix(n)
print(a) 