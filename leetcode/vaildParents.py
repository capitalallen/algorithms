def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        # d = {"(":")","[":"]","{":"}"}
        # stack = []
        # for i in s:
        #     if not stack and i not in d:
        #         return False
        #     if i in d:
        #         stack.append(i)
        #     elif i == d[stack[-1]]:
        #         stack.pop()
        #     else:
        #         return False
        # return len(stack) == 0
            
s= "[["
print(isValid(s))