class Solution:
    def frequencySort(self, s: str) -> str:
        #hashmap freq count
        #put it in heap
        res=""
        hashmap=defaultdict(int)

        for c in s:
            hashmap[c]+=1

        heap=[]
        for key, value in hashmap.items():
            heap.append((-value,key))
        
        heapq.heapify(heap)
        print(heap)

        while heap:
            c=heapq.heappop(heap)
            res+=-c[0]*c[1]
        return res

#time complexity O(NlogN)
#space complexity O(N)