class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        l=0
        r=2*k-1

        def isSorted(nums):
            for i in range(len(nums)-1):
                if nums[i]>=nums[i+1]:
                    return False
            return True


        while r<len(nums):
            mid= (r+l)//2+1
            sub1= nums[l:mid]
            sub2=nums[mid:r+1]
            print(sub1, sub2)
            l+=1
            r+=1

            if isSorted(sub1) and isSorted(sub2):
                return True
        
        return False

#note this is not efficient

#time complex = O(N*K)
#space compelx = O(K)






            