class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        
        def isPal(s, i, j): #constant time
            word= s[i:j+1]
            return word==word[::-1]
        

        def dfs(s,i):
            if i>=len(s):
                res.append(part.copy()) #means a valid combination is found
                return
            
            for j in range(i,len(s)):
                if isPal(s,i,j):
                    part.append(s[i:j+1])
                    dfs(s,j+1) #go through the rest of the string
                    part.pop()
            
        dfs(s,0)
        return res
                

#time complex O(N^2)
#space complex O(N^2)


        
       