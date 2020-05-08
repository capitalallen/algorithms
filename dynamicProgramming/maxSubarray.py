# Kadane's algorithm
class Solution:
    def maxSubArray(self, nums):
        m = nums[0]
        for i in range(1,len(nums)):
            nums[i]=max(nums[i-1],0)+nums[i]
            m = max(m,nums[i])
        return m 
        