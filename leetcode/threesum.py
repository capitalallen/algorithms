def threeSum(numbers):
    # write your code here
    output = []
    l = len(numbers)
    if l <3:
        return []
    numbers = sorted(numbers)
    for i in range(l):
        j = i +1 
        k = l -1
        curr = None
        while j < k:
            curr = numbers[i] + numbers[j] + numbers[k]
            if curr < 0:
                j +=1
            elif curr == 0:
                tmp = [numbers[i],numbers[j],numbers[k]]
                if tmp not in output:
                    print(tmp)
                    output.append(tmp)
                j +=1 
            else:
                k -=1 
    return output
numbers =[-1,0,1,2,-1,-4]
a = threeSum(numbers)
print(a)