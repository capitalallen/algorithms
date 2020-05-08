def mostCommonWord(paragraph,banned):
    ban,words = {},{}
    for i in banned:
        ban[i] = True
    paragraph = paragraph[1:len(paragraph)]
    paragraph = paragraph.split(" ")
    maxLangth,maxwords = 0,""
    special = list("!?',;.")
    for i in paragraph:
        if i[len(i)-1] in special:
                i = i[0:len(i)]
        if i not in ban:
            if i in words:
                words[i] = words[i]+1 
            else:
                words[i] = 1 
            if words[i] > maxLangth:
                maxLangth = words[i]
                maxwords = i 
    return maxwords 
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = "hit"
print(mostCommonWord(paragraph,banned))