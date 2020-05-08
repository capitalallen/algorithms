def orangesRotting(grid):
    r,c = len(grid),len(grid[0])
    count = 0
    queue = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 2:
                queue.append((i,j))
            if grid[i][j] ==1:
                count +=1
    """
    check if no fresh orange: return 0
    
    init: minute and dnr,dnc
    while queue
        for loop: deqeue
            for loop: potential postion
                if valid -> enqueue chagne to rotten 
    """
    if not count:
        return 0
    
    minute = 0
    dnr = [-1,0,1,0]
    dnc = [0,1,0,-1]
    while queue:
        size = len(queue)
        for _ in range(size):
            x,y = queue.pop(0)
            for dr,dc in zip(dnr,dnc):
                nx = x + dr 
                ny = y + dc
                if 0 <= nx <r and 0<=ny<c and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    count -=1
                    queue.append((nx,ny))
        minute +=1
        if count == 0:
            return minute
    return -1