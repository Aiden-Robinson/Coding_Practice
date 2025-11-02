class Solution:
    def reverse(self, x: int) -> int:
        
        rev=0

        sign= -1 if x<0 else 1
        x=abs(x)
        while x!=0:
           
            dig= x%10
            x//=10

            rev=rev*10+dig
            if (rev<-2**31 or rev>2**31-1):
                return 0
            
        
        return sign*rev
        
#time complexity O(log(x))
#space complexity O(1)