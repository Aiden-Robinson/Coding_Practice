class Solution:
    def removeDuplicates(self, s: str) -> str:
        res=[]

        for c in s:
            if res:
                if res[-1]==c:
                    res.pop()
                    continue
            res.append(c)

        
        return "".join(res)

#time complexity O(N)
#space complexity O(N)