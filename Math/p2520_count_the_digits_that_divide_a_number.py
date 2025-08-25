class Solution:
    def countDigits(self, num: int) -> int:
        
        digits=[]

        copy= num

        while copy:
            digits.append(copy%10)
            copy= copy//10
        
        count=0

        for val in digits:
            if num%val==0:
                count+=1
        
        return count
    
#time complexity O(N)
#space complexity O(1)