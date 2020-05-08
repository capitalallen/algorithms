def plusone(digits):
    length = len(digits)
    result = 0
    if length == 1:
        return digits[0] +1
    for i in range(length):
        result += digits[i]*(10**(length-i-1))
    result += 1
    return list(str(result))
print(plusone([1,2,3]))
