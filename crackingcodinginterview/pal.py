def isPalindrome(s):
    def isChar(s):
        s = s.lower()
        ans =''
        for i in s:
            if i in 'qwertyuiopasdfghjklzxcvbnm':
                ans +=i
        return ans
    
    def isPal(s):
        if len(s) <=1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(isChar(s))

a = isPalindrome('asaa')
print(a)
