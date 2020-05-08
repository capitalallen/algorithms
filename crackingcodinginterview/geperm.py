def getPerms(string):
    """
    permutation: record output
    base: len(string) = 0: return " "
    """
    permutation = []
    if string == None:
        return None
    if len(string) == 0:
        permutation.append(' ')
        return permutation
    first = string[0]
    reminder = string[1:]
    words = getPerms(reminder)
    for word in words:
        index = 0
        for letter in word:
            s = insertCharAt(word,first,index)
            if s not in permutation:
                permutation.append(s)
            index +=1
    return permutation
def insertCharAt(word, char, i):
    start = word[:i]
    end = word[i:]
    return start + char + end
    # permutations = []
    # if string == None:
    #     return None
    # if len(string) == 0:
    #     #base case
    #     permutations.append(" ")
    #     return permutations
    # first = string[0] #get first letter in string
    # remainder = string[1:]
    # words = getPerms(remainder)
    # print('first',first,words)
    # for word in words:
    #     print('word:'+str(word))
    #     index = 0
    #     for letter in word:
    #         s = insertCharAt(word, first, index)
    #         print('s: '+ s)
    #         permutations.append(s)
    #         index += 1
    # return permutations
print(getPerms('aabc'))