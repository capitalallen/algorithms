def longestPalindrome(s):
    """
    babad
    
    """
    output = ""
    for i in range(len(s)):
        l = i
        r = -i -1 
        tmp = ""
        while abs(r)<=len(s):
            print(s[l:r],s[::r])
            if s[l:r]==s[::r]:
                tmp = s[l:r]
                continue
            else:
                r -= 1 
        output = tmp if len(tmp)>len(output) else output 
    return output 

s = "babad"
print(longestPalindrome(s))