class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        N=len(code)
        res=[0]*N

        l=0
        curSum=0
        for r in range(N+abs(k)):

            curSum+=code[r%N]

            if r-l+1 > abs(k):
                curSum-=code[l%N]
                l= (l+1) %N
            
            if r-l+1 == abs(k):
                if k>0:
                    res [(l-1)%N]= curSum
                elif k<1:
                    res[(r+1)%N]= curSum
            
        return res

#time complexity O(N)
#Space complexity O(N)
            
            

