class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #window size is actually k+1

        window=set()

        L=0

        for R in range(len(nums)):
            if R-L>k:
                window.remove(nums[L])
                L+=1
            if nums[R] in window:
                return True
            
            window.add(nums[R])
        
        return False
            
    #time complexity O(N), only going through input array once
    #space complexity O(k), set will only ever as big as K
            
            


        


        