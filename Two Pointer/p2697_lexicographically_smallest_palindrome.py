class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
 
        s=list(s)

        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                s[l]= s[r]=min(s[l],s[r])
            l+=1
            r-=1
        
        return "".join(s)

#time complexity O(n)
#space complexity O(n), for the new string at the end
        