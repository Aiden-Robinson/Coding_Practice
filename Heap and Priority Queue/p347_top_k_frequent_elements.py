class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        heap=[]
        res=[]
        hashmap= defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        print(hashmap)

        heapq.heapify(heap)
        for key,val in hashmap.items():
            heapq.heappush(heap,[-val,key])

        print("heap is",heap)
        for i in range(k):
            pair= heapq.heappop(heap)
            res.append(pair[1])

        return res

        
