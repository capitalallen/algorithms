def numIslands(grid):
    if len(grid)==0:
        return 0
    d = {}
    r,c = len(grid),len(grid[0])
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                d[(i,j)]=True
    y = [-1,0,1,0]
    x = [0,-1,0,1]
    s = set()
    for dy,dx in d:
        for dny, dnx in zip(y,x):
            tmpy = dy-dny
            tmpx = dx-dnx
            if 0<=tmpy<r and 0<=tmpx<c:
                tmp = ''.join([str(tmpy),str(tmpx)])
                if grid[tmpy][tmpx] == "1" and tmp not in s:
                    d[(dy,dx)] = False 
                    s.add(tmp)
    count = 0
    for i in d:
        if d[i]:
            count +=1 
    if count==0 and len(d)>0:
        return 1
    else:
        return count
grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
print(numIslands(grid))