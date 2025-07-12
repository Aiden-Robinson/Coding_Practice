class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res=[]

        subset=[]

        def dfs(i):
            if i>= len(nums): #base case
                res.append(subset.copy()) 
                return
            
            #decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #decision to not include nums[i]
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res

            
    #time complexity O(2^n * n), there are 2^n subsets of list n, each element can be included or excluded
    #space complexity O(N) worst case, tis is the recursive depth 