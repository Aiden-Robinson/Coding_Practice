class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        
    
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                print(i,j)
                if nums[i]==nums[j] and (i*j)%k==0:
                    count+=1
        
        return count

    #time complexity O(N^2)
    #space complexity O(1)
