from bisect import bisect

def numSmallerByFrequency(queries, words):
    f = lambda word: word.count(min(word))
    print(f)
    words = sorted(map(f, words))
    # print(words)
    # print(list(map(f, queries)))
    return [len(words) - bisect(words, f(query)) for query in queries]
queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(numSmallerByFrequency(queries,words))