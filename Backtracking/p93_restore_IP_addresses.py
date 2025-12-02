class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        res=[]
        if len(s)>12:
            return res
    
        def backtrack(i, dots, curIp):
            if dots==4 and i==len(s):
                res.append(curIp[:-1])#ignore the last dot
                return
            if dots>4:
                return
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1])<256 and (i==j or s[i]!="0"):
                    backtrack(j+1, dots+1, curIp+s[i:j+1]+".")
            
        backtrack(0,0,"")
        return res

#         time complexity O(3^4) because we have 4 dots and each dot can have 3 choices
#         space complexity O(N) 


        
