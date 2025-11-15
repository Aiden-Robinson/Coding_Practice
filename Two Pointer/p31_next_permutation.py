class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find pivot
        #reverse if there is no pivot

        n=len(nums)

        i=n-2

        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        
        if i<0:
            nums.reverse()#does it in place
            return

        #find the rightmost element greater than i
        j=n-1
        while j>=0:
            if nums[j]>nums[i]:
                break
            else:
                j-=1
        nums[i],nums[j]=nums[j],nums[i]
        nums[i+1:]=reversed(nums[i+1:])
        return
#time complexity O(N)
#space complexity O(1)
        
        
        
