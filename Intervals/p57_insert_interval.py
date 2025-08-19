class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res= []

        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]: #completely before it
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0]>intervals[i][1]: #completely after it
                res.append(intervals[i])
            

            else: #merge

                newInterval= [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
        
        res.append(newInterval)
            
        return res


    #time complexity O(N)
    #space complexity O(1)

            

