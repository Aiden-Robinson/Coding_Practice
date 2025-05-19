class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        window={}
        maxLen=0

        l=0

        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1

            while window[s[r]]>2:
                window[s[l]]-=1
                l+=1
            
            maxLen= max(maxLen, r-l+1)
        
        return maxLen

#time complexity: O(N)
#space complexity O(1)