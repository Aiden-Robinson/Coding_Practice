class Solution:
    def simplifyPath(self, path: str) -> str:

        stack=[]
        cur=""
        for c in path + "/":
            if c == "/": #stop appending to cur when we reach this
                if cur=="..": #go back one directory
                    if stack:
                        stack.pop()
                elif cur!= "" and cur!= ".":
                    stack.append(cur)
                
                cur=""
            
            else:
                cur+=c
        
        return "/" + "/".join(stack) #start with a slash and join all with a slash between
                

#time complexity O(N)
#space complexity O(N)

        