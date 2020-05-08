#O(highest set bit)
def findComplement(num):
    tmp = str(bin(num))[2:]
    result = ""
    for i in tmp:
        if i == '0':
            result +="1"
        else:
            result +="0"
    return int(result,2)
print(findComplement(5))