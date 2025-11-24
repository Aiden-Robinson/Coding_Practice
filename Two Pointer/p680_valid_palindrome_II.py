class Solution:
    def validPalindrome(self, s: str) -> bool:


        def isPal(l,r):
            while l<r:
                if s[r]!=s[l]:
                    return False
                l+=1
                r-=1
            return True
        
        l=0
        r=len(s)-1

        while l<r:
            if s[r]!=s[l]:
                return isPal(l+1,r) or isPal(l,r-1)
            l+=1
            r-=1
        
        return True

#time complexity O(N)
#space complexity O(1)