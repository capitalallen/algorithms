def nextPermutation(nums):
    # write your code here
    """
    [1,3,5,9,6,2]
    [1,3,6,9,5,2]
    [1,3,6,2,5,9]
    start from right side 
    first: find the first number that is smaller than right one 
    find the next biggest number after first 
    swap two number 
    sort the number after the first 
    """
    l = len(nums)
    if l == 0 or l==1:
        return nums
    replace = len(nums)-2
    while replace >=0:
        if nums[replace] < nums[replace+1]:
            break
        replace -=1 
    print(replace)
    if replace <0:
        return nums.sort()
    nextbiggest = replace+1
    while nextbiggest<l-1 and nums[nextbiggest]>nums[replace]:
        print(nextbiggest)
        nextbiggest+=1 
    nums[replace],nums[nextbiggest] = nums[nextbiggest],nums[replace]
    output = nums[0:replace+1] + sorted(nums[replace+1:])
    return output 
nums = [1,2,1]
print(nextPermutation(nums))
            