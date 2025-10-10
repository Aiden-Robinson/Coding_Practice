class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST=defaultdict(str)
        mapTS=defaultdict(str)

        for i in range(len(s)): #they are the same length
            c1,c2= s[i], t[i]


            if ((c1 in mapST and mapST[c1]!=c2) or (c2 in mapTS and mapTS[c2]!=c1)):
                return False

            mapST[c1]=c2
            mapTS[c2]=c1
        
        return True

#time complexity O(N)
#space complexity O(N)