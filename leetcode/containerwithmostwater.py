class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        enumerate height
        init dictionary to store max most water
        iterate through height
        set dict to 0
        go right and left to store max value to dict
        """
        length = len(height)
        left,right = 0,length-1
        max_area, area = 0,0
        while left < right:
            l,r=height[left],height[right]
            if l < r:
                area = (right-left)*l
                while height[left]<=l and left<right:
                    left +=1
            else:
                area = (right-left)*r
                while height[right]<=r and right > left:
                    right-=1
            if area >max_area:
                max_area = area
        return max_area