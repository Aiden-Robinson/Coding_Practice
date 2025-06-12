class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        seen=set()
        repeated=set()

        l=0
        r=10

        while r<=len(s):
            window = s[l:r]

            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)
            r+=1
            l+=1
        

        return list(repeated)
    
    #time complexity O(N)
    #space complexity O(N)


        