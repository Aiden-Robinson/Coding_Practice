class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize !=0:
            return False


        hashmap=defaultdict(int)

        for num in hand:
            hashmap[num]+=1
        
        minH= list(hashmap.keys())

        heapq.heapify(minH)

        while minH:
            smallest= minH[0]
            for i in range(smallest, smallest+groupSize):
                if i not in hashmap:
                    return False
                hashmap[i]-=1
                if hashmap[i]==0: 
                    if i != minH[0]: #you can only pop the minimum element, fails otherwise
                        return False
            
                    heapq.heappop(minH)

        return True


#time complexity O(NLogN)
#space complexity O(N)




       

        

        
        