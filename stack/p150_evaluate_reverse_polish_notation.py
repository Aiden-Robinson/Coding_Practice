class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for c in tokens:
            if c== '+':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(op1+op2)

            elif c== '-':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(op1-op2)
            elif c=='*':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(op1*op2)
                pass
            elif c== '/':
                op2=stack.pop()
                op1=stack.pop()
                stack.append(int(op1/op2))

            else:
                stack.append(int(c))

        
        return stack[0]
            

#time complexity O(N)
#space complexity O(N)