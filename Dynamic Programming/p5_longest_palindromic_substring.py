class Solution:
    def longestPalindrome(self, s: str) -> str:

        res=""
        resLen=0

        for i in range(len(s)):
            l,r=i,i #for an odd length

            while l>= 0 and r< len(s) and s[l]==s[r]: # it is a palindrome
                if (r-l+1)>resLen:
                    resLen= r-l+1
                    res= s[l:r+1]
                
                l-=1
                r+=1
    
            l,r=i,i+1 #for an odd length

            while l>=0 and r<len(s) and s[l]==s[r]: # it is a palindrome
                if (r-l+1)>resLen:
                    resLen= r-l+1
                    res= s[l:r+1]
                
                l-=1
                r+=1
        
        return res

    #time complexity O(N)
    #space complexity O(1)
        
        