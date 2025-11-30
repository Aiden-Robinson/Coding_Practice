class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS= len(matrix)
        COLS= len(matrix[0])

        cache={} #key= (r,c) value= length

        def helper(r,c):
            if r>=ROWS or c>=COLS: #base case
                return 0
            
            if (r,c) not in cache:
                bottom= helper(r+1,c)
                right= helper(r,c+1)
                diag= helper(r+1, c+1)
                cache[(r,c)]=0 #default value
                if matrix[r][c]=="1":
                    
                    cache[(r,c)]= 1+ min(bottom, right, diag)

            return cache[(r,c)]
        
        helper(0,0)
        return max(cache.values())**2

#time complexity O(N*M)
#space complexity O(N*M)