class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        res=0
        hashMap=defaultdict(int)

        
        l=0
        for r in range(len(s)):
            hashMap[s[r]]+=1

            while (r-l+1)- max(hashMap.values())>k:
                hashMap[s[l]]-=1
                l+=1
            res= max(res, r-l+1)
        
        return res
        
        
#time complexity O(26*N) because to get the max of all values in the hashmap, there are at most 26 values
#space complexity O(1)
        



        

        

        