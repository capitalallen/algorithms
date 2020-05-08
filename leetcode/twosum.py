"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""
def twoSum(nums,target):
	diff = {target-nums[i]:i for i in range(len(nums))}
	return [ [n, diff[nums[n]]] for n in range(len(nums)) if nums[n] in diff and n != diff[nums[n]]][0]

nums = [2, 7, 11, 15]
target = 9
twoSum(nums,target)