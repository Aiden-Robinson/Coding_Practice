class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #two stacks, iterate both strings, pop when #occurs

       
        
        def build(string):
            stack=[]
            for c in string:
                if c=="#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            
            return stack


        return build(s)==build(t) 

#time complexity O(N)
#space complexity O(N)