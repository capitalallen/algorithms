def searchMatrix(matrix,target):
    if len(matrix)==0:
        return False
    if not matrix[0]:
        return False
    row,last = 0,len(matrix[0])-1
    l,r=0,len(matrix)-1
    if target > matrix[r][last]:
        return False
    while l<=r:
        m=int((l+r)/2)
        if matrix[m][last]==target:
            return True
        elif matrix[m][last]<target:
            l = m+1 
        else:
            r = m-1 
    row = l 
    if matrix[row][last]<target and row <len(matrix):
        row+=1 
    l,r=0,len(matrix[row])-1
    while l<=r:
        m=int((l+r)/2)
        if matrix[row][m]==target:
            return True 
        elif matrix[row][m]<target:
            l =m+1 
        else:
            r = m-1 
    return False 
matrix = [[]]
target=1888
print(searchMatrix(matrix,target))