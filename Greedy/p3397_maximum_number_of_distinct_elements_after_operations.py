class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        count=0
        lastUsed= -float('inf')

        for num in nums:
            candidate= max(num-k, lastUsed+1)
            if candidate<=num+k:
                count+=1
                lastUsed=candidate
            
        
        return count
    
#time complexity O(N)
#space complexity O(1)
