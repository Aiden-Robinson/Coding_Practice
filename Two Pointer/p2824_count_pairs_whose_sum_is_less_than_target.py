class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort() #O(N logN)
        l=0
        r= len(nums)-1

        count=0
        while l<r: #O(N)
            if nums[l]+nums[r]<target:
                count+=r-l
                l+=1
            else:
                r-=1
        
        return count

#time complexity O(N LogN)
#space complexity O(1)

#suboptimal
        # count=0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i<j and nums[i]+nums[j]<target:
        #             count+=1

        # return count
        