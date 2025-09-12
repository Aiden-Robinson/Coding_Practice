class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        offset=1

        for i in range(1, n+1):
            if offset*2==i: #if we've reached a new factor of 2
                offset=i
            
            dp[i]= 1 + dp[i-offset]
        
        return dp

    #time complexity O(N)
    #space complexity O(1)




        