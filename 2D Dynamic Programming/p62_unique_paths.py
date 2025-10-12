class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        row=[1]*n

        for i in range(m-1): #not actually building top down
            newRow= [1]*n
            for j in range(n-2,-1,-1):
                newRow[j]= newRow[j+1]+row[j]
            
            row=newRow
        
        return row[0]

#time complexity: O(m*n)
#space complexity: O(n)