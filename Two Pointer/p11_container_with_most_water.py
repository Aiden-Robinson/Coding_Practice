class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=0

        def getArea(l,r):
            width= r-l
            length= min(height[l], height[r])
            return width*length
        
        while r>=l:
            area= getArea(l,r)
            res= max(res,area)
            print(l,r,area)

            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res

#time complexity O(N)
#space complexity O(1)



       


        