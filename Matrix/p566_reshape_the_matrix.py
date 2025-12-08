class Solution:

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS= len(mat)
        COLS= len(mat[0])

        if ROWS*COLS != r*c:
            return mat
        
        res=[]
        curCol=[]
        for i in range(ROWS):
            for j in range(COLS):
                curCol.append(mat[i][j])

                if len(curCol)==c:
                    res.append(curCol)
                    curCol=[]
        
        print(res)
        return res

#time complexity O(ROWS*COLS)
#space complexity O(ROWS*COLS)