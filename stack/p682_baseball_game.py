class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack=[]

        for c in operations:
            try:
                stack.append(int(c))
            
            except ValueError:
                if c=='+':
                    stack.append(stack[-1]+stack[-2])
                elif c=='D':
                    stack.append(stack[-1]*2)
                elif c=='C':
                    stack.pop()
                
        ans=0
        for num in stack:
            ans+=num
        
        
        return ans

#time complexity O(N)
#space complexity O(N)
       