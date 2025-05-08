class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        sMap= {}
        tMap={}

        for c in s:
            sMap[c]= sMap.get(c,0)+1
        
        for c in t:
            tMap[c]=tMap.get(c,0)+1
        
        print(sMap)
        print(tMap)

        added=""
        for key,val in tMap.items():
            if val>sMap.get(key,0):
                added=key
                return added
        
        
        
#time complexity: O(N)
#space complecity O(N)

#optimized solution, uses ord values because 
'''
  result = 0
        for c in s:
            result ^= ord(c)
        for c in t:
            result ^= ord(c)
        return chr(result)

'''

#XOR uses a^a=0 so any difference will be pointed out
        

    
        