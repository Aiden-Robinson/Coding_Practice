class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        #find monotomocs stack

        stack=[]
        
    
        for x in num:
            
            while k>0 and stack and stack[-1]>x:
                k-=1
                stack.pop()
            stack.append(x)

        stack=stack[:len(stack)-k]
        res="".join(stack)
        res = res.lstrip("0")

        return res if res else "0"

        #time complexity O(N)
        #space complexity O(N)  