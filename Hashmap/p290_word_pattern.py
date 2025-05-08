class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        tracker={}
        words= s.split(" ")
        
        if len(pattern) != len(words):
            return False

        wordToChar={}
        charToWord={}

        for c, w in zip(pattern, words): #lets us iterate through both at same time
            if c in charToWord and charToWord[c]!=w:
                return False
            if w in wordToChar and wordToChar[w]!=c:
                return False
            wordToChar[w]=c
            charToWord[c]=w
        return True

        #time complexity O(n+m)
        #space complexity O(n+m)