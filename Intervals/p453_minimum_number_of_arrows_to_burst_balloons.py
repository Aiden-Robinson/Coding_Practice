class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[0])
        res= len(points)
        prev=points[0]

        for i in range(1,len(points)):
            curr= points[i]

            if prev[1]>=curr[0]:
                prev= [curr[0], min(curr[1],prev[1])]
                res-=1
            else:
                prev=curr
        
        return res

#time complexity O(N logN)
#space complexity O(1)