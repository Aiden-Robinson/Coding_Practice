class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            res+= n%2 #check the last bit of n, if its an odd number(last bit is 1), res will ad 1
            n=n >>1 #discard the last bit now
        return res

    #time complexity O(N)
    #space complexity O(1)