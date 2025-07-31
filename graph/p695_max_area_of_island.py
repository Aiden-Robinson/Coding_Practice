class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS= len(grid)
        COLS= len(grid[0])

        seen=set()
        

        def dfs(r,c):
            if r<0 or r>=ROWS or c<0 or c >=COLS or grid[r][c]==0 or (r,c) in seen:
                return 0
            
        
            seen.add((r,c))
            area=1

            area+=dfs(r+1, c)
            area+=dfs(r-1, c)
            area+=dfs(r, c+1)
            area+=dfs(r, c-1)
            return area
        
        area=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1 and (i,j) not in seen:
                    area=max(area, dfs(i,j))
        return area

    #time complexity O(N*M)
    #space complexity O(N*M)

            
