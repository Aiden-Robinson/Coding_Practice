class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0

        for num in nums:
            res ^=num #XOR all the numbers together, the numbers that appear twice will cancel out, leaving only the number that appears once
        return res
    
    #time complexity O(N)
    #space complexity O(1)