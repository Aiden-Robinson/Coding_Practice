class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask= 0xFFFFFFFF
        while b: #if b is 0 there is no carry and we are done
           temp= (a^b) & mask #sum without carry
           b= ((a & b) <<1) & mask #carry
           a= temp
        

        #handle negative numbers
        return a if a <= 0x7FFFFFFF else ~(a^ mask)