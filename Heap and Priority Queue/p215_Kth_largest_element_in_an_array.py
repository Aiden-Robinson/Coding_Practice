class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

    
        maxHeap= [-num for num in nums]
        heapq.heapify(maxHeap)
        
        for i in range (k-1):
            heapq.heappop(maxHeap)
        
        return -maxHeap[0]


        #time complexity O(N+ KlogN)
        #space complexity O(N)
        #alternate solution
        
        #minHeap= []
        # for num in nums:
        #     heapq.heappush(minHeap,num)
        #     if len(minHeap)>k:
        #         heapq.heappop(minHeap)
        
        # return minHeap[0]