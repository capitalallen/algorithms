def indent(n):
    for i in range(n):
        print("    ",end="")
def permute(nums):
    def backtrack(first=0):
        # indent(first)
        # print('backtrack(first=',first,')',nums)
        if first == n:
            output.append(nums[:])
        for i in range(first,n):
            nums[first],nums[i] = nums[i],nums[first]
            backtrack(first+1)
            nums[first],nums[i] = nums[i],nums[first]      
    n = len(nums)
    output = []
    backtrack()
    return output
nums = ["g","o","o","g","l","e"]
print(permute(nums))