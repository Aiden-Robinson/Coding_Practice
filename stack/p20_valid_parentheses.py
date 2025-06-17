class Solution:
    def isValid(self, s: str) -> bool:
    
        bMap={')':'(', '}':'{',']':'[' }

        stack=[]

        for char in s:
            if char in bMap:
                if stack and stack[-1]==bMap[char]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(char)
        
        print(stack)
        if not stack:
            return True
        return False
        

#time complexity O(N)
# space complexity O(N)