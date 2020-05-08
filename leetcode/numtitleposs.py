def numTilePossibilities(tiles):
    """
    :type tiles: str
    :rtype: int
    """

    res = set()
    def dfs(path, t):
        print('dfs(',path,'|',t,")")
        if path:
            print('path:',path)
            res.add(path)
        for i in range(len(t)):
            dfs(path+t[i], t[:i] + t[i+1:])  
    dfs('', tiles)
    print(res)
    return len(res)
tiles = 'AAB'
print(numTilePossibilities(tiles))
