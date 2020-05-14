class Solution:
    def sortArray(self, nums):
        return self.margeSort(nums)
    
    def margeSort(self,nums):
        # divide
        if len(nums)<=1:
            return nums
        p = int(len(nums)/2)
        left = self.margeSort(nums[0:p])
        right = self.margeSort(nums[p:len(nums)])
        return self.marge(left,right)
    def marge(self,leftList,rightList):
        newList = []
        l,r = 0,0
        while l <len(leftList) and r < len(rightList):
            if leftList[l] < rightList[r]:
                newList += [leftList[l]]
                l+=1
            else:
                newList += [rightList[r]]
                r += 1
        newList.extend(leftList[l:])
        newList.extend(rightList[r:])
        return newList