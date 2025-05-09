class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        ans=[]
        for word in words:
            for row in rows:
                if all( c in row for c in word.lower()): #sees if all iterations are true
                    ans.append(word)
                    break
        return ans

#time complexity O(n) because it is just 3 strings which is a constant number
#space complexity O(n)

        
      
        