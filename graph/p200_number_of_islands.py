class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS= len(grid)
        COLS= len(grid[0])

        seen=set()
        count=0

        def dfs(r, c):
            if r<0 or r>=ROWS or c<0 or c>=COLS or (r,c) in seen or grid[r][c]=='0':
                return
            
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]=='1' and (i,j) not in seen:
                    count+=1
                    dfs(i,j)

        return count

    #time complexity O(N*M)
    #space complexity O(N*M)