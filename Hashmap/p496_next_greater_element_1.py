class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans=[]
        n=len(nums2)
        
        for num in nums1:
            start= nums2.index(num)
            found= False
            for i in range(start+1,n):
                if nums2[i]>num:
                    ans.append(nums2[i])
                    found=True
                    break
            if found==False:
                ans.append(-1)
        
        return ans
            

#time complexity: O(m*n) m is length of nums1 and n is length of nums2
#space complexity: O(m) m is the space of nums1, space req for ans







        