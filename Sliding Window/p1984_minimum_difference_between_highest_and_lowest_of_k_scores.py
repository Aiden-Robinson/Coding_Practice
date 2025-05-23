class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        minDiff= float('inf')

        nums.sort()
        l=0
        r=k-1

        while r<len(nums):
            diff = nums[r]-nums[l]
            minDiff= min(minDiff,diff)
            l+=1
            r+=1
        
        return minDiff

#time complexity O(NLogN)
#space complexity O(1)





        