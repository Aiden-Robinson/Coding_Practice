class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res=0
        hashmap=defaultdict(int)
        

        def divideconq(s):
            if len(s)<k:
                return 0
            hashmap=defaultdict(int)
            for c in s:
                hashmap[c]+=1
            
            splitOn=[]
            for key, val in hashmap.items():
                if val<k:
                    splitOn.append(key)
            
            if not splitOn:
                return len(s)
            import re
            pattern= f"[{''.join(splitOn)}]"
            parts= re.split(pattern,s)

            candidates=[divideconq(part) for part in parts if part]
            return max(candidates,default=0)
        
        res= divideconq(s)
        return res
        
#time complexity O(N^2)
#space complexity O(N)
