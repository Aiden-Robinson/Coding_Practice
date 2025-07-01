class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Hash= defaultdict(int)

        for c in s1:
            s1Hash[c]+=1
        
        print(s1Hash)
        
        windowHash=defaultdict(int)

        #initially populate 
        l=0
        r=0
        while r< len(s2):
            windowHash[s2[r]]+=1
            
            if r-l+1>len(s1): #ensure window size is correct 
                windowHash[s2[l]]-=1
                if windowHash[s2[l]]==0: #removes garbage from the window 
                    del windowHash[s2[l]] 
                l+=1
            
            
            if windowHash == s1Hash:
                return True
            r+=1
        
        return False

#time complexity O(N+M), the dictionary comparision is O(26)
#space complexity O(1), dictionaries are efficient 