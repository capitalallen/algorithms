class Solution:
    def totalNQueens(self, n: int) -> int:
        
        
        def notUnderAttack(row,col):
            return (not r[row]) and (not c[col]) and (not dal[row-col]) and (not hil[row+col])
        
        def placeQueen(row,col):
            r[row],c[col] = 1, 1
            dal[row-col],hil[row+col] = 1,1
        
        def removeQueen(row,col):
            r[row],c[col] = 0,0
            dal[row-col],hil[row+col] = 0,0
            
        def backtrack(row,count):
            for col in range(n):
                if notUnderAttack(row,col):
                    placeQueen(row,col)
                    if row+1 == n:
                        count += 1
                    else:
                        count = backtrack(row+1,count)
                    removeQueen(row,col)
            return count
        r = [0]*n
        c = [0]*n
        dal = [0]*(n*2)
        hil = [0]*(n*2)
        return backtrack(0,0)