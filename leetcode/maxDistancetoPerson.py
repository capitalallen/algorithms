import math
def maxDistToClosest(seats):
    """
    
    3 scanerios:
        start with 0: [0,0,0,1]
        between 1: [1,0,0,1]
        end with 0: [1,0,0,0]
    available: store number of 0 from each interval 
    [3,2,3]
    count =0
    
    stack is empty:
            count +=1
    condition:
        if i !=1:
            count +=1
        if i ==1 and stack is empty:
            stack.append(i)
            continue 
        
        stack is not empty:
            if i ==1:
                stack.pop()
                available.append()
                count = 0
                
    """
    if not seats:
        return 0
    a = ''
    for i in seats:
        a += str(i) 
    
    seats = a.split('1')
    print(seats)


    first = len(seats[0]) if a[0] == 0 else 0
    end = len(seats[len(seats)-1]) if a[len(a)-1]==0 else 0
    
    maxSeats = 0
    for i in seats[1:len(seats)-1]:
        if len(i)>maxSeats:
            maxSeats = len(i)
    print(end)
    return max(first,end,int(math.ceil(maxSeats/2)))
    