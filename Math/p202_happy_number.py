class Solution:
    def isHappy(self, n: int) -> bool:
        
        def sumdigits(n):
            total=0
            while n>0:
                total+=(n%10)**2
                n//=10
            return total
        
        seen=set()

        while True:
            if n in seen:
                return False
            if n==1:
                return True
            seen.add(n)
            n= sumdigits(n)
        
#time complexity O(log n)
#space complexity O(log n)