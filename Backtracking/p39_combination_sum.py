class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]

        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            #include it in decision
            cur.append(candidates[i])
            dfs(i, cur, total+ candidates[i])
        
            #backtrack
            cur.pop()
            dfs(i+1,cur, total)
        
        dfs(0,[],0)
        return res
#time complexity O(2^T), 2 decisions to be made-> branching factor of 2, smallest candidate is 1
#space complexity O(T)