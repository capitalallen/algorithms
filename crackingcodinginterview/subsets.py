def subsets(nums):
    res = []
    helper(nums, 0, res, [])
    return res

def helper(nums, idx, res, aux):
    if idx == len(nums):
        res.append(aux.copy())
        print(res)
        return
    print('helper(',nums,idx,res,aux,')')
    aux.append(nums[idx])
    helper(nums, idx + 1, res, aux)
    aux.pop()
    helper(nums, idx + 1, res, aux)

def subsets1(nums):
    res = [[]]
    for i in nums:
        print(res,i)
        res += [s + [i] for s in res]
    return res
nums = [1,2,3]
a = subsets1(nums)
print(a)