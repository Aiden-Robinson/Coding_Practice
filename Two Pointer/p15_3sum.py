class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        target=0
        res=[]
        a=0

        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]: #if theres a duplicate just move on 
                continue
            l=a+1
            r=len(nums)-1

            while l<r:
                total= nums[a]+nums[l]+nums[r]

                if total>target:
                    r-=1
                elif total <target:
                    l+=1
                elif total==target:
                    res.append([nums[a],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    
        
        return res

#time complexity O(N^2)
#space complexity O(1)