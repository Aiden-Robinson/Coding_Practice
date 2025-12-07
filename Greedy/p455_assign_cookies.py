class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res=0

        pChild, pCook=0,0

        while pChild<len(g) and pCook<len(s):
            if s[pCook]>=g[pChild]:
                res+=1
                pChild+=1
                pCook+=1
            else:
                pCook+=1
        
        return res

#time complexity O(NLogN)
#space complexity O(1)