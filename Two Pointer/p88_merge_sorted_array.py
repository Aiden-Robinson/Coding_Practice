class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res=[]
        p1,p2=0,0

        a=nums1[:m]

        while p1<m and p2<n:
            if a[p1]<nums2[p2]:
                res.append(a[p1])
                p1+=1
            else:
                res.append(nums2[p2])
                p2+=1
            
        res+=a[p1:]
        res+=nums2[p2:]
        
        for i in range(n+m):
            nums1[i]=res[i]

    #time complexity O(N+M)
    #space complexity O(N+M)