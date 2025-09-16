class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res=0

        for num in nums:  #XOR all the numbers together, the numbers that appear twice will cancel out, leaving only the number that appears once
            res^=num
        
        for i in range(len(nums)+1): #XOR all the numbers from 0 to n, the numbers that appear twice will cancel out, leaving only the number that appears once
            res^=i
        
        return res

#time complexity O(N)
#space complexity O(1)
