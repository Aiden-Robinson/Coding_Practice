class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        

        l=0
        r=len(nums)-1
    
        unique= set()
        while l<r:
            unique.add((nums[l]+nums[r])/2.0)
            l+=1
            r-=1
        
        
        return len(unique)

#time compexity: O(nlogn), its actually NLogN + N but simplifies to NLogN
#space complexity O(n)
        