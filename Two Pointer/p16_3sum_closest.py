class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best= float('inf')
        res=0

        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue #skip duplicates
            
            l=a+1
            r=len(nums)-1

            while l<r:
                total= nums[a]+nums[l]+nums[r]
                diff = abs(total-target)
                
                if diff<best:
                    best= diff
                    res=total
                
                if total>target:
                    r-=1
                elif total<target:
                    l+=1
                else:
                    return total
        return res
                

#time complexity O(N^2)
#space complexity O(1)