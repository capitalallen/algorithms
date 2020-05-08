def fizzBuzz(n):
    if n == 0:
        return []
    if n == 1:
        return ["1"]
    if n ==2:
        return ["1","2"]
    result = ["1","2"]
    for i in range(3,n+1):
        if i%3 == 0 and i%5==0:
            result.append("FizzBuzz")
        elif i%3 ==0:
            result.append("Fizz")
        elif i%5 ==0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzBuzz(5))