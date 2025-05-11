class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """

        target= (sum(aliceSizes)-sum(bobSizes))/2 #each is O(n) and O(m) to sum
        print(target)
        
        for u in set(aliceSizes):
            if u-target in set(bobSizes):
                return [u, u-target]

        #time complexity O(n+m)
        #memory complexity O(n+m)


        