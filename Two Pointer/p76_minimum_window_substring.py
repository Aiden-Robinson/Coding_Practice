class Solution:
    #not optimal but I pretty much did it myself
    def minWindow(self, s: str, t: str) -> str:
        hashS=defaultdict(int)
        hashT=defaultdict(int)
        res=""
        min_len=float("inf")

        for c in t:   #fills t 
            hashT[c]+=1
        print("hashT ", hashT)
        

        r,l=0,0

        def valid(hashS,hashT):
            valid=True
            for key in hashT.keys():
                if hashS[key]<hashT[key]:
                    valid=False
            return valid


        while r<len(s):
            hashS[s[r]]+=1

            while(valid(hashS,hashT)):
                if r-l+1<min_len:
                    min_len=r-l+1
                    res=s[l:r+1]
                hashS[s[l]]-=1
                l+=1

            r+=1
        
        return res
        
# time compelxity O(s*t)
# space complexity O(s+t)
# 