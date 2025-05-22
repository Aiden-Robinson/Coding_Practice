class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        count=0

        
        for i in range (len(s)):
            substring= s[i:i+3]
            window= set(substring)
            if len(window)==3:
                count+=1
        
        return count

        
        #time complexity O(N)
        #space complexity O(1)
     
        
        
        