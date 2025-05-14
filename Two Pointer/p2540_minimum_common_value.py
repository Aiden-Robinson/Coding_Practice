class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        i,j=0,0

        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                return nums1[i]
            elif nums1[i]>nums2[j]:
                j+=1
            elif nums2[j]>nums1[i]:
                i+=1
        
        return -1

#time complexity O(N+M)
#space complexity O(1)


 #my solution, which is slightly slower
        # lowest= float('inf')

        # r1= len(nums1)-1
        # r2=len(nums2)-1

        # while r1>=0 and r2>=0:
        #     if nums1[r1]==nums2[r2]:
        #         lowest=min(lowest,nums1[r1])
        #         r1-=1
        #         r2-=1
        #     elif nums1[r1]>nums2[r2]:
        #         r1-=1
        #     elif nums2[r2]>nums1[r1]:
        #         r2-=1
        # if lowest ==float('inf'):
        #     return -1
        
        # return lowest
