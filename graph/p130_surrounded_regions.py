class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS= len(board)
        COLS= len(board[0])
        

        def capture(r,c):
            if (r<0 or r==ROWS or c<0 or c==COLS or board[r][c]!="O" ): #only if its a 0
                return
            board[r][c]="T"
            
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        
        for r in range(ROWS): #only check if its an edge
            for c in range(COLS):
                if board[r][c]=="O" and (r in [0,ROWS-1] or c in [0, COLS-1]):
                    capture(r,c)
        

        for r in range(ROWS): #convert all 0's to exes
            for c in range(COLS):
                if board[r][c]=="O":
                    board[r][c]="X"
        
        for r in range(ROWS): #convert all T's to 0's
            for c in range(COLS):
                if board[r][c]=="T":
                    board[r][c]="O"
                

#time complexity O(N*M)
#space complexity O(1)
            
        

        