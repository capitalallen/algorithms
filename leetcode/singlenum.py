def singleNumber(nums):
    return 2*sum(set(nums)) - sum(nums)

print(singleNumber([2,2,1]))