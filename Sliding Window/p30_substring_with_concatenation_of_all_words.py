class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordlen= len(words[0]) #all word lengths are the same
        res=[]

        basemap=defaultdict(int)
        for word in words:
            basemap[word]+=1
        
        total_len=wordlen*len(words)

        l=0

        for i in range(0,len(s)-total_len+1):
            window=s[i:i+total_len]
            comparemap=defaultdict(int)
            for j in range(0,total_len,wordlen):
                
                miniwindow= window[j:j+wordlen]
                comparemap[miniwindow]+=1
            
            if comparemap==basemap:
                res.append(i)
           
        return res

#not the most efficient solution
#time complexity: O(n*m)
#space complexity: O(n+m)