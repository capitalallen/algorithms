def spiralOrder(matrix):
    """
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]   
    [1,2,3,6,9,8,7,4,5]
    input: 2D list
    output: spiral order 1D list
    edge: empty list
    
    for loop with two while loop 
    """
    if not matrix:
        return matrix
    output = []
    left,top = 0,0
    right,bottom = len(matrix[0])-1,len(matrix)-1
    
    while left < right and top < bottom:
        for i in range(left,right):
            output.append(matrix[top][i])
        for i in range(top,bottom):
            output.append(matrix[i][right])
        for i in reversed(range(left+1,right+1)):
            output.append(matrix[bottom][i])
        for i in reversed(range(top+1,bottom+1)):
            print(matrix[i][left])
            output.append(matrix[i][left])
        left+=1
        right-=1
        top+=1
        bottom-=1
        
    if left == right:
        print('left')
        for i in range(top,bottom+1):
            print("-->",i)
            output.append(matrix[i][left])
    elif bottom == top:
        print('right')
        for i in range(left,right):
            output.append(matrix[top][i])
    
    return output 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))