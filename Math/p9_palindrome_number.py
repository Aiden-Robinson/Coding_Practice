class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False

        #solving without converting to string

        digits=[]

        while x:
            digits.append(x%10)
            x=x//10
        
        return digits==digits[::-1]
    

#time complexity O(log10(x))
#space complexity O(log10(x))