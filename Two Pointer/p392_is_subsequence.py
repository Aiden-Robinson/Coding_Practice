class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps, pt=0,0

        if not s:
            return True

        while pt<len(t):
            if t[pt]==s[ps]:
                ps+=1
            
            if ps==len(s):
                return True
            
            pt+=1
        
        return False

#time complexity O(N)
#space complexity O(1)