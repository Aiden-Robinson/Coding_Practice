class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0

        for num in nums:
            res ^=num
        return res
    
    #time complexity O(N)
    #space complexity O(1)