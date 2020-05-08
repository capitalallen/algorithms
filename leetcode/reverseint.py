def reverseint(x):
        out = int(str(abs(x))[::-1]) if x > 0 else int(str(abs(x))[::-1]) * -1
        return out if out in range(-2**31, 2**31 - 1) else 0
print(reverseint(123))

        # y = str(x)
        # neg = False
        # length = len(y) -1
        # if y[0] == '-':
        #     y = y[1:len(y)]
        #     neg = True
        # y = int(y[::-1])
        # if (neg):
        #     y = -y
        # if y in range(-2**31, 2**31 - 1):
        #     return(y)
        # else:
        #     return 0

