from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def placeNum(d,row,col):
            rows[row][d] +=1
            cols[col][d] += 1
            boxes[boxIndex(row,col)][d]+=1
            board[row][col] = str(d)
            
        def removeNum(row,col,d):
            del rows[row][d]
            del cols[col][d]
            del boxes[boxIndex(row,col)][d]
            board[row][col] = '.'
            
        
        def couldPlace(row,col,d):
            return not (d in rows[row] or d in cols[col] or d in boxes[boxIndex(row,col)])
        def backtrackHelper(row,col):
            if col ==N-1 and row == N-1:
                nonlocal solved
                solved = True
            else:
                if col == N -1:
                    backtrack(row+1,0)
                else:
                    backtrack(row,col+1)
                
        def backtrack(row=0,col=0):
            if board[row][col] == '.':
                for i in range(1,10):
                    if couldPlace(row,col,i):
                        placeNum(i,row,col)
                        backtrackHelper(row,col)
                        if not solved:
                            removeNum(row,col,i)
            else:
                backtrackHelper(row,col)
        
        n = 3 
        N = 3*3 
        solved = False
        boxIndex = lambda row, col: (row//3)*n + col//3 
        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] !='.':
                    d = int(board[i][j])
                    placeNum(d,i,j)
        backtrack()