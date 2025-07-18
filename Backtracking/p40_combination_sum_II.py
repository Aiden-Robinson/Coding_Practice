class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()

        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            
            if i==len(candidates) or total>target:
                return

            #include current index
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            
            #exclude current index
            cur.pop()
            
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i+=1
            dfs(i+1, cur, total)
        
        dfs(0,[],0)
        return res
    
    #time complexity O (N * 2^N)
    #space compelxity O(N)