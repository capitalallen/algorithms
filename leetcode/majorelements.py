def majorityNumber(nums):
    # write your code here
    """
    l: length of nums 
    use pointer 
    count: count occurance of a num 
        -> if more than l/2 return the num 
        [1,2,2,2]
    """
    nums = sorted(nums)
    l = len(nums)
    count = 0 
    t = 0 
    print(nums)
    tmp = 0
    for i in range(l-1):
        j = i +1 
        print(i,nums[i],nums[j])
        print(i,' count:',count)
        if nums[i] == nums[j]:
            count +=1 
            tmp = count
        else:
            count =0
        if tmp + 1>=l/2:
            return nums[i]
    print('output')
    return t
nums = [2,2,2,1]
print(majorityNumber(nums))
