class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        mod= s.split(" ")
        
        for i in range(len(mod)-1,-1,-1):
            if mod[i]:
                return len(mod[i])
                


#time complexity O(N)
#space complexity O(N)