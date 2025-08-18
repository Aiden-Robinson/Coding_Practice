class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res=max(nums)
        curMax=1
        curMin=1

        for n in nums:
            tmp= curMax*n
            curMax= max(curMax*n, curMin*n, n)
            curMin= min(tmp, curMin*n, n)

            res=max(res, curMax)
        
        return res

#time complexity O(N)
#space complexity O(1)