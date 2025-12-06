class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globMax, globMin= nums[0], nums[0] #just set it to something

        curMax,curMin= 0,0
        total=0

        for n in nums:
            curMax= max(n, curMax+n)
            curMin= min(n, curMin+n)

            total+=n
            globMax= max(globMax, curMax)
            globMin= min(globMin, curMin)
        
        return max(globMax, total-globMin) if globMax>0 else globMax
    
    #time complexity O(N)
    #space complexity O(1)