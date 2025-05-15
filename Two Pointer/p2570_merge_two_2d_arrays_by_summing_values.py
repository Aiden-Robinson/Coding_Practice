class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """

        print(nums1[0])
       
        res=[]
        i,j=0,0
        while i<len(nums1) and j<len(nums2):
            if nums1[i][0]== nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0]> nums2[j][0]:
                res.append([nums2[j][0],nums2[j][1]])
                j+=1
                
            elif nums1[i][0]< nums2[j][0]:
                res.append([nums1[i][0],nums1[i][1]])
                i+=1


        #if theres still some leftover

        while i< len(nums1):
            res.append([nums1[i][0],nums1[i][1]])
            i+=1
        while j<len(nums2):
            res.append([nums2[j][0],nums2[j][1]])
            j+=1
        
                
      
        return res
        

#time complexity O(n+m)
#space complexity O(n+m), because we created a new array of this size to store answer
            
        