class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS=defaultdict(int)
        hashT= defaultdict(int)

        for c in s:
            hashS[c]+=1
        
        for c in t:
            hashT[c]+=1
        
        if hashT==hashS:
            return True
        
        return False
    
#time complexity O(N + M)
#space complexity O(N+M)
