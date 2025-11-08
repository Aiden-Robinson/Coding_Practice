class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        #heap
        n=len(matrix)

        minheap=[]
        heapq.heapify(minheap)

        for r in range(n):
            heapq.heappush(minheap,(matrix[r][0],r,0))
        
        for i in range(k-1):
            val, r, c= heapq.heappop(minheap)

            if c+1<n:
                heapq.heappush(minheap, (matrix[r][c+1],r,c+1))
        
        return heapq.heappop(minheap)[0]


        
        print(minheap)

#time complexity O(NlogN)
#space complexity O(N)