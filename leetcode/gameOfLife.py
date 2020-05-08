def gameOfLife(board):
    # Neighbors array to find 8 neighboring cells for a given cell
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
    rows = len(board)
    cols = len(board[0])
    boardCopy = [[board[row][col] for col in range(cols)] for row in range(rows)] 
    for i in range(rows):
        for j in range(cols):
            liveNeighbor = 0
            for neighbor in neighbors:
                row = i + neighbor[0]
                col = j + neighbor[1]
                if (row<rows and row >=0) and (col<cols and col >=0) and (boardCopy[row][col]==1):
                    liveNeighbor +=1
            if boardCopy[i][j] == 1 and (liveNeighbor<2 or liveNeighbor>3):
                board[i][j] =0
            if boardCopy[i][j] == 0 and liveNeighbor==3:
                board[i][j] =1
    return board
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
a = gameOfLife(board)
print(a)                