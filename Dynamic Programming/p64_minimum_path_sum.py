class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])


        dp=[[0]*COLS for i in range(ROWS)]

        dp[ROWS-1][COLS-1]= grid[ROWS-1][COLS-1]


        for r in range(ROWS-1,-1,-1):
            for c in range(COLS-1,-1,-1):
                # don't overwrite bottom-right
                if r == ROWS - 1 and c == COLS - 1:
                    continue
                
                fromtop= dp[r+1][c] if r<ROWS-1 else float('inf')
                fromleft= dp[r][c+1] if c<COLS-1 else float('inf')

                dp[r][c]= grid[r][c]+ min(fromtop, fromleft)
        
        return dp[0][0]

#time complexity O(N*M)
#space complexity O(N*M)