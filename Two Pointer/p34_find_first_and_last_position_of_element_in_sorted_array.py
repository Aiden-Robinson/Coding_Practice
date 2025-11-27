class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findfirst():
            l,r= 0, len(nums)-1
            ans=-1

            while l<=r:
                mid= (l+r)//2
                if nums[mid]==target:
                    ans=mid
                    r=mid-1
                elif nums[mid]<target:
                    l=mid+1
                    
                else:
                    r=mid-1
            return ans

        def findlast():
            l,r= 0, len(nums)-1
            ans=-1

            while l<=r:
                mid= (l+r)//2
                if nums[mid]==target:
                    ans=mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                    
                else:
                    r=mid-1
            return ans
        
        first=findfirst()
        last=findlast()

        if first ==-1:
            return [-1,-1]
        return [first, last]
        #time complexity O(logN)
        #space complexity O(1)

        #naive approach
        # l=0
        # r=len(nums)-1

        # while l<len(nums):
        #     if nums[l]==target:
        #         break
        #     l+=1
        # while r>0:
        #     if nums[r]==target:
        #         break
        #     r-=1

        # if (l==len(nums) and r==0) or not nums:
        #     return [-1,-1]
        
        # return [l,r]

#time complexity O(N)