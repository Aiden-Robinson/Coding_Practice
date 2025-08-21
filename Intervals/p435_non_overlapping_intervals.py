class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[0])
        print(intervals)

        count=0
        prevUBound= float('-inf')
        
        for i in range(len(intervals)):

            if intervals[i][0]<prevUBound:
                count+=1
                prevUBound=min(intervals[i][1],prevUBound)
                continue
            

            prevUBound= intervals[i][1]
        
        return count

    #time complexity O(NLogN)
    #space complexity O(1)
