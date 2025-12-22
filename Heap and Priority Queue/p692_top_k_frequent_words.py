class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #hashmap
        #heap
        res=[]
        hashmap= defaultdict(int)
        for word in words:
            hashmap[word]+=1
        
        
        heap=[]
        heapq.heapify(heap)

        for key, val in hashmap.items():
            heapq.heappush(heap, (-val,key))
        
        for i in range(k):
            word= heapq.heappop(heap)[1]
            res.append(word)
        
        return res


       

#time complexity O(NlogN)
#space complexity O(N) 