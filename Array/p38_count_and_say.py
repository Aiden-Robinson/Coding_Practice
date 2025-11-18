class Solution:
    def countAndSay(self, n: int) -> str:

        
        if n==1:
            return "1"
        
        cur = self.countAndSay(n-1) #returns a string
        #sliding window
        res=""
        count=1

        for i in range(1,len(cur)):
            if cur[i]==cur[i-1]:
                count+=1
            else:
                res+=f"{count}{cur[i-1]}"
                count=1
        
        res+=f"{count}{cur[-1]}"
        return res