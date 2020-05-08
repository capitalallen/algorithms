def fourSum(nums, target):
    """
    input array
    output 2d array
    edge case: empty list
    
    solution
    """
    output = []
    nums = sorted(nums)
    for first in range(len(nums)):
        last = len(nums)-1
        second = first +1 
        while second < last:
            third = second + 1
            lastCopy = last 
            while third < lastCopy:
                tmp = nums[first]+nums[second]+nums[third]+nums[lastCopy]
                if tmp > target:
                    lastCopy -=1 
                elif tmp < target: 
                    third +=1
                else:
                    output.append([nums[first],nums[second],nums[third],nums[lastCopy]])
                    third +=1 
            second += 1
    return output 
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))
    