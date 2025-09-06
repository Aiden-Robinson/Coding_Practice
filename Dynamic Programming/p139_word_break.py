class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      

    

        dp=[False]* (len(s)+1)
        dp[len(s)]= True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w))<=len(s) and s[i:i+len(w)]==w:
                    dp[i]= dp[i+len(w)]
                if dp[i]: #don't need to check it agian for other words in wordDict
                    break
                
        return dp[0]

    #time complexity O(N * M *K), 
    #space complexity O(N)
