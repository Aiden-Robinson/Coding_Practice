class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows= len(matrix)
        cols= len(matrix[0])

        top= rows-1
        bot= 0

        if target<matrix[bot][0] or target > matrix[top][-1]:
            return False

        while bot<=top:
            m= (top+bot)//2
            if target > matrix[m][-1]:
                bot= m+1
            elif target < matrix[m][0]:
                top= m-1
            else:
                break
        
        mid= (top+bot)//2
        search= matrix[mid]
        

        l=0
        r=cols-1
        

        while l<=r:
            m= (l+r)//2
            if target> search[m]:
                l=m+1
            elif target < search[m]:
                r= m-1
            else:
                return True
        
        return False
        
#time complexity O(Log(N*M))
#space complexity O(1)


