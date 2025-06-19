class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack=[]

        for c in s:
            stack.append(c)
            if c.isdigit():
                stack.pop()
                if stack and not stack[-1].isdigit():
                    stack.pop()
        

        return ''.join(stack)

    #time complexity O(N)
    #space complexity O(N)