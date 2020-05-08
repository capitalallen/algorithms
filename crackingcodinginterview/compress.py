def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    if len(chars) == 0:
        return 0
    elif (len(chars)) == 1:
        return 1
    d = {}
    res = []
    for i in range(len(chars)):
        if chars[i] in d:
            d[chars[i]] = d[chars[i]] + 1
        else:
            d[chars[i]] = 1
    for i in d:
        res.append(str(i))
        res.append(str(d[i]))
    return res
chars = ["a","a","b","b","c","c","c"]
a = compress(chars)
print(a)