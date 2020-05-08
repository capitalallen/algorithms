def strStr(self, haystack: str, needle: str) -> int:
    if not needle:
        if needle == haystack:
            return 0
        return 0
    elif not haystack:
        return -1 
    if needle in haystack:
        i = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                temp = i
                t = needle[0]
                for j in range(1,len(needle)):
                    temp +=1
                    if needle[j] == haystack[temp]:
                        t += haystack[temp]
                if t == needle:
                    return i
    else:
        return -1