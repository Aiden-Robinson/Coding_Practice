
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #values to the left
        prefix=[1]*len(nums)
        for i in range(1,len(nums)):
            prefix[i]*=nums[i-1]*prefix[i-1]

        #values to the right
        postfix=[1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            postfix[i]*=nums[i+1]*postfix[i+1]
       
        for i in range(len(postfix)):
            postfix[i]*=prefix[i]
        
        return postfix

#time complexity O(N)
#space complexity O(1), the result array is not part of the memory in this problem