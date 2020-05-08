def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    a = 0
    r = len(s) -1
    while a < r:
        while a < r and not s[a].isalnum():
            a +=1
        while a < r and not s[r].isalnum():
            r -= 1
        if s[a].lower() != s[r].lower():
            return False
        a+=1
        r -=1
    return True
s = "0P"
a = isPalindrome(s)
print(a)