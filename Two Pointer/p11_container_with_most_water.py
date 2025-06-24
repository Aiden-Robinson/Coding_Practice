class Solution:
    def maxArea(self, height: List[int]) -> int:

    
        # store the distance from first line to line itself as w
        #take the minumum height of any two vertical lines

        def getArea(ind1, ind2)->int: #O(N)
            w=abs(ind1-ind2)
            h=min(height[ind1], height[ind2])
            return w*h
        

        l=0
        r=len(height)-1
        maxArea=0

        while l<r:
            area= getArea(l,r)
            maxArea=max(maxArea,area)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        
        return maxArea
            

#time complexity O(N)
#space complexity O(1)



       


        