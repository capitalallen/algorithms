def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    result = ''
    l = [len(st) for st in strs]
    for i in range(min(l)):
        tmp = [j[i] for j in strs]
        if min(tmp) == max(tmp):
            result += tmp[0]
        else: 
            return result
# edge cases


# length of all words

# loop through the word with min letters

# if lo
List = ["flower","flighe","flow"]
print(longestCommonPrefix(List))


# Input: ["flower","flighe","flow",'f']
#fle
#flighe
"""
f f f
l l l
o o -
"""
# Output: "fl"