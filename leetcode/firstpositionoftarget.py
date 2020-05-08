def binarySearch(nums, target):
    # write your code here
    l,r=0,len(nums)
    if r ==0:
        return -1
    r -=1 
    while l<=r:
        m = int((l+r)/2)
        tmp = nums[m]
        if tmp==target:
            while m>=0 and tmp==target:
                #m-=1 
            m = m+1 if tmp != target else m
            return m
        elif nums[m]<target:
            l = m+1 
        else:
            r = m-1 
    return -1 
nums=[1,4,4,5,7,7,8,9,9,10]
target =1 
print(binarySearch(nums,target))