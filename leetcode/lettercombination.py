def letterCombinations(digits):
    phoneNum = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
    def allCombination(combination,nextDigits):
        print('allCombination(',combination,' | ',nextDigits,')')
        if len(nextDigits) == 0:
            output.append(combination)
            print(output)
        else:
            for i in phoneNum[nextDigits[0]]:
                allCombination(combination + i,nextDigits[1:])
    output = []
    if digits:
        allCombination("",digits)
    return output
digits = "23"
print(letterCombinations(digits))