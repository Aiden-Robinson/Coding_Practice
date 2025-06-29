class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l=0
        r=1
        bestP=0

        while r < len(prices):
            if prices[r]>prices[l]:
                bestP=max(bestP, prices[r]-prices[l])
            
            else:
                l=r
            r+=1
        
        return bestP

#time complexity O(N)
#Space complexity O(1)