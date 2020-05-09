class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        input: list
        output: reversed list
        two pointers: one from 0 position, another one from the end
        tmp: store end temporialy 
        """
        start,end = 0,len(s)-1
        def helper(start,end):
            if start < end:
                s[start],s[end] = s[end],s[start]
                helper(start+1,end-1)
        helper(start,end)
        return s 

s = Solution()
print(s.reverseString(["a","b","c"]))
