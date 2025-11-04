class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp=[0]*(amount+1)
        dp[0]=1 #there is only one way to make up a 0 amount

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]+= dp[i-coin]
        
        return dp[amount]

#time complexity O(N*M)
#space complexity O(N)