class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtrack(curr = 1,res=[]):
            # base case: if len(res)!=k
            # for i in range(curr,n+1) append to res, backtrack(i,res)
            # else append to output, remove last element from res 
            if len(res)!=k:
                for i in range(curr,n+1):
                    backtrack(i+1,res+[i])
            else:
                output.append(res[:])
                res.pop()
        output = []
        backtrack()
        return output