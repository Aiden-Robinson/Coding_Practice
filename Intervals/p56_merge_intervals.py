class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        print(intervals)
        res=[]

        i=0
        while i< (len(intervals)):

            lowBound=intervals[i][0]
            highBound=intervals[i][1]
            while i+1<len(intervals) and highBound>=intervals[i+1][0]:
                highBound=max(highBound, intervals[i+1][1])
                i+=1
            i+=1
            
            res.append([lowBound,highBound])

        
        return res


   
            
#time complexity O(NLogN), from the sorting
#space complexity O(N)


            