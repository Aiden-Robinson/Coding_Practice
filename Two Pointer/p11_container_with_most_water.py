class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res=0
        l=0
        r=len(height)-1
        def getArea(l,r):
            return min(height[l],height[r])*(r-l)
        while l<r:
            res= max(res,getArea(l,r))
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
      

        return res


#time complexity O(N)
#space complexity O(1)



       


        
