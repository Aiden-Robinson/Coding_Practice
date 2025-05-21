class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def isNice(s):
            chars=set(s)
            return all(c.lower() in chars and c.upper() in chars for c in chars)

        
        
        maxLen=0
        niceString=""
        for r in range(len(s)):
            l=0
            
            while l<=r:
                substring=s[l:r+1]

                if isNice(substring):
                    if len(substring)>maxLen:
                        maxLen=len(substring)
                        niceString=substring
                        break
                l+=1
        return niceString

        #time complexity O(N^3)
        #space complexity O(N)

        #this is a complete shit show of a question


        # my attempt
        # maxLen=0
        # niceString=""
        
        # window=set()

        # l=0

        # for r in range(len(s)):
        #     window.add(s[r])
        #     while (s[r].upper() not in window) and (s[r].lower() not in window):
        #         window.remove(s[l])
        #         l+=1
            
            
        #     if r-l>maxLen:
        #         maxLen=r-l
        #         niceString=s[l:r]
        
        # return niceString
       

        