class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        longest=0

        l=0

        for r in range(1,len(nums)):
            while nums[r]-nums[l]>1:
                l+=1

            if nums[r]-nums[l]==1:
                longest=max(r-l+1,longest)
        
        return longest


#time complexity O(NLogN)
#space complexity O(1)

        


        
        