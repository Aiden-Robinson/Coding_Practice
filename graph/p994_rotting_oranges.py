class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS= len(grid)
        COLS= len(grid[0])

        q= deque()

        fresh=0

        for r in range(ROWS): #prework
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                
                if grid[r][c]==2:
                    q.append([r,c])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        time=0
        while q and fresh>0:
            for i in range(len(q)): #go through everything in the queue
                r,c= q.popleft()

                for dr, dc in directions:
                    row= r+dr
                    col=c+dc

                    if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            time +=1
        
        return time if fresh==0 else -1


#time complexity O(N*M)
#space comlextiy O(N*M)


                
            
                

