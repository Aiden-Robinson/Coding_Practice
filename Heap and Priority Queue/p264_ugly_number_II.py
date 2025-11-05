class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minheap=[1]
        heapq.heapify(minheap)
        seen=set()
        factors=[2,3,5]

        for i in range(n):
            num= heapq.heappop(minheap)
            if i ==n-1:
                return num
            
            for f in factors:
                if (num*f) not in seen:
                    heapq.heappush(minheap,(num*f))
                    seen.add(num*f)
                
#time complexity O(NlogN)
#space complexity O(N)