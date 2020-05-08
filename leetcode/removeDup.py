"""
input: list
output: int
c: optimize
e: empty list
"""
def removeDuplicates(nums):
    #empty list return 0
    #tmp = list pop
    #if tmp in list remove tmp from list
    #push tmp back to list

    length = len(nums)
    if length ==0:
        return 0
    for i in range(length):
        tmp = nums.pop(0)
        if tmp in nums:
            nums.remove(tmp)
        nums.append(tmp)
    return len(nums)
nums =[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
nums =[1,1,2]
print(removeDuplicates(nums))