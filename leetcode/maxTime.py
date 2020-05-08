def maxTime(s):
    UndifinedDigits = [False]*4
    digits = []
    for i in s:
        if i != ":":
            digits.append(i)
    print(digits)
    for i in range(len(digits)):
        if digits[i] == "?":
            UndifinedDigits[i] = True 
    if UndifinedDigits[3]:
        digits[3] = "9"
    if UndifinedDigits[2]:
        digits[2] = "5"
    if UndifinedDigits[0] and UndifinedDigits[1]:
        digits[0],digits[1]="2","3"
    elif UndifinedDigits[0] and not UndifinedDigits[1]:
        if int(digits[1])>3:
            digits[0] = 1
        else:
            digits[0] = 2 
    elif not UndifinedDigits[0] and UndifinedDigits[1]:
        if int(digits[0]) ==2:
            digits[1]="3"
        else:
            digits[1]="9"
    output = "{}{}:{}{}"
    return output.format(digits[0],digits[1],digits[2],digits[3])

s =["?4:5?","23:5?","2?:22","0?:??","??:??","1?:??"]
for i in s:
    print(maxTime(i))

        
