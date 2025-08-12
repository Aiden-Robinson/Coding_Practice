class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        
        def distance(x,y):
            return sqrt(x**2+y**2)

        return heapq.nsmallest(k, points, key= lambda p: distance(p[0],p[1]))

        
    #time complexity O(N logK)
    #space complex O(k)
