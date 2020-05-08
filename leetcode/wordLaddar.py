import collections
def ladderLength(start, end, di):
    # write your code here
    """
    build a graph {0:(1,3)}
    iterate through dict 
        convert each dict to set 
        build the graph 
        
    """
    if not end or not start or not di:
        return 0
    L = len(start)
    
    all_combo_dict = collections.defaultdict(list)
    for i in range(L):
        all_combo_dict[end[:i]+"*"+end[i+1:]].append(end)
    for word in di:
        for i in range(L):
            all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)
    print(all_combo_dict)
    queue = collections.deque([(start,1)])
    visited = {start:True}
    while queue:
        current_word, level = queue.popleft()
        for i in range(L):
            intermediate_word = current_word[:i] + "*"+current_word[i+1:]
            
            for word in all_combo_dict[intermediate_word]:
                if word ==end:
                    return level+1
                if word not in visited:
                    visited[word] = True
                    queue.append((word,level+1))
            all_combo_dict[intermediate_word]=[]
    return 2
start ="hit"
end = "cog"
di =["hot","dot","dog","lot","log"]
print(ladderLength(start,end,di))