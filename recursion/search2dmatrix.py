def searchMatrix(matrix):
    #base case: left >right or up > down:
    if not matrix:
        return 
    printMatrix(0,len(matrix[0])-1,0,len(matrix)-1,matrix)
def printMatrix(left,right,top,bottom,matrix):
    print(left,right,top,bottom)
    if left > right or top > bottom:
        return False
    midCol = (right+left)//2
    midRow = (top+bottom)//2
    for i in range(top,bottom+1):
        print(matrix[i][left:right+1])
    return printMatrix(left,midCol-1,top,midRow,matrix) or printMatrix(midCol,right,top,midRow,matrix) or printMatrix(left,midCol-1,midRow+1,bottom,matrix) or printMatrix(midCol,right,top,midRow,matrix)
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]

searchMatrix(matrix)
