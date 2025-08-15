class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        

        count= Counter(tasks)
        maxHeap=[-num for num in count.values()]
        heapq.heapify(maxHeap)
        queue= deque() #[cnt, time]
        time=0

        

        while maxHeap or queue:
            time+=1
            if maxHeap:
                cnt= 1+ heapq.heappop(maxHeap) #subtracts one from the max
                if cnt:
                    queue.append([cnt, time+n])
            
            if queue and queue[0][1]==time: #it's time to process whats in the queue, first in line
                heapq.heappush(maxHeap, queue.popleft()[0]) #put remainder back in heap
        
        return time
    
    #time complexity O(N*M)
    #space complex O(N)
            
            



        