class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curSum=0

        for i in range(k):
            curSum+=nums[i]
        
        highest=curSum/k

        for i in range(k,len(nums)): #continue where you left off
            curSum+=nums[i] #adjusting window
            curSum-=nums[i-k]
            
            highest=max(highest, curSum/k)

        return highest

#time complexity: O(N)
#space complexity O(1)
        
        

        