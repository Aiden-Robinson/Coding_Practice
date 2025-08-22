class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res= max(nums)
        curMax=0

        for num in nums:
            curMax= max(num, num+curMax)
            res= max(curMax,res)
        
        return res


#time complexity O(N)
#space compelxity O(1)