class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n= len(nums)
        used= [False]*n
        ans, sol=[],[]
       

        def backtrack():
            if len(sol)==n:
                ans.append(sol.copy())
                return
            
            for i in range(n):
                if used[i]: #skip this index if we've used it
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1] : #skip duplicate, need to be sortes for this
                    continue
                
                used[i]=True
                sol.append(nums[i])
                backtrack()
                sol.pop()
                used[i]=False
        
        backtrack()
        return ans

#time complexity O(N * N!)
#space complexity O(N)