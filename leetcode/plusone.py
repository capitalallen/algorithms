def plusOne(nums):
        if len(nums) == 1:
            return nums[0]
        #max_end and max_sofar
        max_end = 0
        max_sofar = -99999
        #for loop
        for i in range(len(nums)):
            max_end += nums[i]
            #if max_sofar < max_end --> max_sofar == max_end and append
            if max_sofar < max_end:
                max_sofar = max_end
            #if max_end <0 --> 0
            if max_end < 0:
                max_end = 0
        return max_sofar
print(plusOne([-2,-1]))
"""
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""