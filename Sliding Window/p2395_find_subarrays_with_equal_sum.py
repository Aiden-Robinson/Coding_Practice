class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        hashset=set()
        curSum=0

        for l in range(len(nums)-1):
            r=l+1
        
            curSum= nums[l]+nums[r]
            if curSum in hashset:
                return True
            else:
                hashset.add(curSum)
            
            curSum-=nums[l]
        
        return False
            
            
    #time complexity O(N)
    #space complexity O(N)
