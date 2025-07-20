class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res= []

        subset=[]
        nums.sort()

        def dfs(i):
            if i== len(nums):
                res.append(subset.copy())
                return

            #include it
            subset.append(nums[i])
            dfs(i+1)


            #don't include it
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return res

    #time complexity O(N * 2^n)
    #space complexity O(N)
    