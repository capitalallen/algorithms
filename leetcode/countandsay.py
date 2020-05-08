def countAndSay(n):
    if n == 1:
        return '1'
    elif n ==2:
        return '11'
    result = '11'
    for i in range(3,n+1):
        result+='$'
        l = len(result)
        tmp = ""
        count = 1
        for j in range(1,l):
            if result[j] == result[j-1]:
                count +=1
            else:
                tmp += str(count)
                tmp += str(result[j-1])
                count = 1
        result = tmp
    return result
print(countAndSay(5))
"""
 1.     1
 2.     11
 3.     21
 4.     1211a
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
"""