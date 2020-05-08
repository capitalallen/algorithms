def lengthOfLongestSubstring(s):
    temp = set('')
    i = 0
    for x in s:
        print(x)
        # if in temp, return i
        if (x in temp):
            return i
        # else append and increment i
        else:
            temp = temp | set(x)
            i += 1



#input "pwwkew"
s = "pwwkew"
#output #4
print(lengthOfLongestSubstring(s))
