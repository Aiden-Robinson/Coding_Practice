class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        
        #normalize such that it always goes clockwise
        if start>destination:
            start,destination= destination, start

        countF=0
        #loop1
        for i in range(start,destination):
            countF+=distance[i]
        
        print(countF)

        total=0
        for num in distance:
            total+=num
        
        countB=total-countF

        return min(countF, countB)

#time complexity O(N)
#space complexity O(1)