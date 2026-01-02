class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]: #completely before
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]: #completely after
                res.append(intervals[i])
            
            else: #me
                newInterval= (min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1]))
            
        res.append(newInterval)

        return res



    #time complexity O(N)
    #space complexity O(1)

            

