class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        #everytime the stack is 0 

        retStr=[]
        balance=0
        for c in s:
            if c=='(':
                if balance>0:
                    retStr.append(c)
                balance+=1
            else:
                balance-=1
                if balance>0:
                    retStr.append(c)
                
        
        return "".join(retStr)

    #time complexiy O(N)
    #space complexity O(N)

        