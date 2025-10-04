class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap= defaultdict(int)

        for c in magazine:
            hashmap[c]+=1
        
        print(hashmap)

        for c in ransomNote:
            if c not in hashmap or hashmap[c]==0:
                return False
            
            hashmap[c]-=1
        
        return True

#time complexity O(n+m)
#space complexity O(m)