class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        answer=[1]*n

        prefix=1

        for i in range(n):
            answer[i]=prefix
            prefix*=nums[i]

        postfix=1
        for i in range(n-1, -1, -1):
            answer[i]*=postfix
            postfix*=nums[i]

        return answer
        
#time complexity O(N)
#space complexity O(1), the result array is not part of the memory in this problem