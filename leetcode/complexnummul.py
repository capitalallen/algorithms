def complexNumberMultiply(a, b):
    """
    a:"1+-11i"
    b:"0+0i"
           a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)
    """

    a = a.split('+')
    b = b.split('+')
    t1 = int(a[0])*int(b[0])
    t2 = int(a[0])*int(b[1][:-1])+int(b[0])*int(a[1][:-1])
    t3 = (int(a[1][:-1])*int(b[1][:-1]))*(-1)
    print(t1,t2,t3)
    a = t1 + t3
    b = t2
    if a <0:
        a = '-' + str(abs(a))
    else:
        a = str(a)
    if b < 0:
        b = '-' + str(abs(b))
    else:
        b = str(b)
    return (a+'+'+b+'i')
a="1+-1i"
b="0+0i"
c = complexNumberMultiply(a,b)
print(c)

