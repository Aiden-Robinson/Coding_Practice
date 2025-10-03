class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

        #time complexity O(N)
        #space complexity O(1)
        
        
        # s=s.split(" ")
        
        # s_clean=[]
        # for word in s:
        #     if word:
        #         s_clean.append(word)
            
        # s_clean=s_clean[::-1]

        # res=""

        # for i in range(len(s_clean)-1):
        #     res+=s_clean[i]
        #     res+=" "
        
        # res+=s_clean[-1]
        
        # return res