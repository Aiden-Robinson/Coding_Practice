class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap= defaultdict(list)
        for u, v, w in times:
            hashmap[u].append((v, w))
        
        minheap=[(0,k)]
        t=0

        seen=set()

        while minheap:
            w1, n1= heapq.heappop(minheap)
            if n1 in seen:
                continue
            seen.add(n1)
            t= max(t,w1)

            for n2, w2 in hashmap[n1]:
                if n2 not in seen:
                    heapq.heappush(minheap,(w2+w1, n2))
                
        
        if len(seen)==n:
            return t
        else:
            return -1

            

#time complexity O(E*logv)
#space complex O(V+E)


        

        