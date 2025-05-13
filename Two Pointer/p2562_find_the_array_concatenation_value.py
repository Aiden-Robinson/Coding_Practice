class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l=0

        r= len(nums)-1

        concat=0
        while l<=r:
            if l==r:
                concat+=nums[l]
            else:
                concat+= int(str(nums[l])+str(nums[r]))
            
            l+=1
            r-=1
        
        return concat

#Time complexity O(N)
#Space complexity O(1)            