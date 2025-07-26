class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1,rob2=0,0

        for i in range(1,len(nums)): #go through array once
            temp= max(rob1+nums[i],rob2)
            rob1= rob2
            rob2=temp
        
        rob3, rob4= 0,0

        for i in range(len(nums)-1): #go through array second time
            temp= max(rob3+nums[i],rob4)
            rob3= rob4
            rob4=temp
        
        return max(rob2, rob4, nums[0])

        #time complexity O(N)
        #space complexity O(1)