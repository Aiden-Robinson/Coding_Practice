class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:

        indicies= [i for i,x in enumerate(nums) if x==target]

        res=float('inf')

        for ind in indicies:
            res= min(res, abs(ind-start))
        
        return res
        
        #time complexity O(N)
        #space complexity O(N)